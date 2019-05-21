<?php
define('CALLBACK_API_EVENT_CONFIRMATION', 'confirmation');
define('CALLBACK_API_EVENT_MESSAGE_NEW', 'message_new');
define('CALLBACK_API_EVENT_MESSAGE_REPLY','message_reply');
//no keyboard
define('MON_SHORT','понедельник');
define('TUE_SHORT','вторник');
define('WED_SHORT','среда');
define('THU_SHORT','четверг');
define('FRI_SHORT','пятница');
define('SAT_SHORT','суббота');
define('HZ2','сегодня');
//no keyboard
define('MON','Понедельник😰');
define('TUE','Вторник😓');
define('WED','Среда😱');
define('THU','Четверг🙄');
define('FRI','Пятница😏');
define('SAT','Суббота🤗');
define('HZ','Какой сегодня день?🤷‍♀️');

define('FOTO','📸');

include_once 'config.php';
require_once 'global.php';
require_once 'res/keyboard.php';
require_once 'api/vk_api.php';
require_once 'api/yandex_api.php';

require_once 'bot/bot.php';

require_once 'jsonDB.php';
require_once BOT_CLASS_DIRECTORY.'/schedule.php';






if (!isset($_REQUEST)) {
  exit;
}
$fileName="res/my.db";
$bd = new bd($fileName);
callback_handleEvent();

function callback_handleEvent() {
  $event = _callback_getEvent();

  try {
    switch ($event['type']) {
      //Подтверждение сервера
      case CALLBACK_API_EVENT_CONFIRMATION:
        _callback_handleConfirmation();
        break;

      //Получение нового сообщения
      case CALLBACK_API_EVENT_MESSAGE_NEW:
        _callback_handleMessageNew($event['object']);
        break;
	  case CALLBACK_API_EVENT_MESSAGE_REPLY: 
	  
	  break;
      default:
        _callback_response('Unsupported event');
        break;
    }
  } catch (Exception $e) {
    log_error($e);
  }

  _callback_okResponse();
}

function _callback_getEvent() {
  return json_decode(file_get_contents('php://input'), true);
}

function _callback_handleConfirmation() {
  _callback_response(CALLBACK_API_CONFIRMATION_TOKEN);
}
function rewriteNoKeyboardStyle($msg){
	switch ($msg){
		case MON_SHORT:
			return MON;
		break;
		case TUE_SHORT:
			return TUE;
		break;
		case WED_SHORT:
			return WED;
		break;
		case THU_SHORT:
			return THU;
		break;
		case FRI_SHORT:
			return FRI;
		break;
		case SAT_SHORT:
			return SAT;
		break;
		default:
			return $msg;
		break;
	}
}
function _callback_handleMessageNew($data) {
	global $bd;
	global $keyboards;
	$user_id = $data['peer_id'];
	if ($bd->isRegistered($user_id)){
		//$bd->deleteUser($user_id);
		
		$update_data = "---Данные обновлены---\n%name%, теперь ты будешь видеть расписание для %group% подгруппы.\nЧтобы изменить свою подгруппу наведи 'меню'.";
		
		$sch = new schedule(BOT_BASE_DIRECTORY.'/res/schJSON.json');
		
		$group=$bd->getUserGroup($user_id);
		$users_get_response = vkApi_usersGet($user_id);
		$user = array_pop($users_get_response);
		$user_name = $user['first_name'];
		$data['text'] = (stripos($data['text'], HZ2) === false) ? $data['text'] : HZ;//if send "сегодня"
		$data['text'] = rewriteNoKeyboardStyle($data['text']);//no keyboard style
		if ($data['text']==MON || $data['text']==TUE ||$data['text']==WED||$data['text']==THU||$data['text']==FRI||$data['text']==SAT||$data['text']==HZ){

				$dateDay = getDayDate(msgDayToNum($data['text']));
				$chWeek = $sch->isChWeek($dateDay) ? "ч/н":"н/н";
				$msg_dop=numToDayRu(msgDayToNum($data['text'])).' '.$dateDay->format("d.m.Y").' '.$chWeek."\n-------------------------\n";

				$sch_str=$sch->getDaySheduleText($dateDay,$group);
				$msg = $msg_dop.$sch_str;
				//if ($data['text']==HZ){log_msg($msg);}
				//log_msg($msg);
				//$bd->updateGroup($user_id,1);
				bot_sendMessage($user_id,$msg,NULL,$keyboards['days']);
		}else if ($data['text']==CHANGE_GROUP){
			$msg = "Выбери подгруппу.";
			bot_sendMessage($user_id,$msg,NULL,$keyboards['groups']);
		}else if ($data['text']=="09-641 (1)" || $data['text']=="09-641 (2)"){
			$grNum = $data['text']=="09-641 (1)" ? 1 : 2;
			$bd->updateGroup($user_id,$grNum);
			$msg = str_replace('%name%',$user_name,$update_data);
			$msg = str_replace('%group%',$grNum,$msg);
			bot_sendMessage($user_id,$msg,NULL,$keyboards['days']);
		}else if ($data['text']==FOTO || mb_strtolower($data['text']) == 'фото'){
			bot_sendSchPhoto($user_id,$keyboards['days']);
		}else if (mb_strtolower($data['text'])==mb_strtolower("Меню") || mb_strtolower($data['text'])==mb_strtolower(START)){

			$msg = "Меню";
			
			bot_sendMessage($user_id,$msg,NULL,$keyboards['menu']);
		}
			$log_srt=$user_name.' - '.$data['text'];
			log_msg($log_srt);
	  #echo "registered".$group;
	}else{
		$first_start = "Привет, %name%!\nЯ подскажу тебе расписание на любой день и буду присылать важную информацию)\n Описание:\n 🎧 - так обозначаются лекции\n🔌 - так обозначаются лабы\nНапиши боту:\n меню - чтобы открыть меню бота.\n фото -  присылает полное фото расписания.\n📌Чтобы просмотреть расписание необходимо выбрать подгруппу.";
		$save_data = "---Данные сохранены---\n%name%, теперь ты будешь видеть расписание для %group% подгруппы.\nЧтобы изменить свою подгруппу наведи 'меню'.";
		
		$users_get_response = vkApi_usersGet($user_id);
		$user = array_pop($users_get_response);
		$user_name = $user['first_name'];
		
		if ($data['text']==START){
			$msg = str_replace('%name%',$user_name,$first_start);
			bot_sendMessage($user_id,$msg,NULL,$keyboards['groups']);
		}else if ($data['text']=="09-641 (1)" || $data['text']=="09-641 (2)"){
			$grNum = $data['text']=="09-641 (1)" ? 1 : 2;
			$bd->addUser($user_id,$user_name,$grNum);
			$msg = str_replace('%name%',$user_name,$save_data);
			$msg = str_replace('%group%',$grNum,$msg);
			bot_sendMessage($user_id,$msg,NULL,$keyboards['days']);
		}else if ($data['text']=="[club177859022|Расписание] фото"){
			bot_sendSchPhoto($user_id,NULL);
		}else{
			$msg = str_replace('%name%',$user_name,$first_start);
			bot_sendMessage($user_id,$msg,NULL,$keyboards['groups']);
		}
			$log_srt=$user_id.' - '.$data['text'];
			log_msg($log_srt);
	}
	_callback_okResponse();
}

function _callback_okResponse() {
  _callback_response('ok');
}

function _callback_response($data) {
  echo $data;
  exit();
}


