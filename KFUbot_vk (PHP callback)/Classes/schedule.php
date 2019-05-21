<?
Class schedule{
	public $schJSON;
	public $file;
	public $timeLessonFizRa=Array("8.00-9.30","10.00-11.30","12.00-13.30","14.00-15.30","16.00-17.30","16.00-17.30","16.00-17.30");
	public $timeLesson=Array("8.30-10.00","10.10-11.40","11.50-13.20","14.00-15.30","15.40-17.10","17.20-18.50","19.00-20.30");
	public $startLessonDate;
	//public $dateStartLessons=date(2019, 2, 7)
	function __construct($file){
		$j = file_get_contents($file); // в примере все файлы в корне
		$data = json_decode($j,true); 
		$this->schJSON=$data;
		$this->startLessonDate = new DateTime('2019-02-07');
	}
	function getSchJSON(){
		return $this->schJSON;
	}
	function getDaySheduleText($date=0,$group=1){
		$numDay = $date->format('N')-1;
		$s='';
		$chWeek = $this->isChWeek($date) ? "second_cn":"first_nn";
		
		for ($i=0;$i<count($this->schJSON[$this->numToDay($numDay)]);$i++){
			$lessonStr = $this->schJSON[$this->numToDay($numDay)][$i][$chWeek]["group".$group];
			$emptyLesson =empty($lessonStr) ? " --" : "";
			$s.=$this->numToEmoji($i+1).$this->getTimeLesson($i,$lessonStr).$emptyLesson.$lessonStr."\n";
		}
		return $s;
	}
	function getTimeLesson($num,$title){
		$fizRa = "УНИКС";
		return (strpos($title, $fizRa) === false) ? $this->timeLesson[$num] : $this->timeLessonFizRa[$num];
	}
	function numToEmoji($num){
		$emodzi_num=Array('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟');
		return $emodzi_num[$num];
	}
	function numToDay($num){
		$weekDays=Array("monday","tuesday","wednesday","thursday","friday","saturday","sunday");
		return $weekDays[$num];
	}
	function isChWeek($date){
		$weekStart = $this->startLessonDate->format('W');
		$weekDate = $date->format('W');
		if (($weekDate - $weekStart)%2==0){
			return False;
		}else{
			return True;
		}
	}
}
function msgDayToNum($str){
	switch ($str){
		case MON:
			return 0;
		break;
		case TUE:
			return 1;
		break;
		case WED:
			return 2;
		break;
		case THU:
			return 3;
		break;
		case FRI:
			return 4;
		break;
		case SAT:
			return 5;
		break;
		case HZ:
			$today = new DateTime();
			return 	$today->format("N")-1;
		break;
	}
}
	function numToDayRu($num){
		$weekDays=Array("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье");
		return $weekDays[$num];
	}
function getDayDate($num){
	$today = new DateTime();
	$diff = abs($num+1 - $today->format("N"));
	if ($num+1 < $today->format("N")){
		//next week
		$diff = 7 - $diff;
		$today->modify('+'.$diff.' day');
	}else{
		//this week
		$today->modify('+'.$diff.' day');

	}
	return $today;
}

?>