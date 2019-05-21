import vk_api
import requests
import random
import openpyxl
import modules.bd as database
import json
import res.strings as s
import modules.scheduleClass as sched
from vk_api.utils import get_random_id
import modules.settings as settings
from datetime import datetime,date,timedelta




bd = database.bd("my.db")
session = requests.Session()
login, password = settings.vk_login, settings.vk_pass
vk_session = vk_api.VkApi(token=settings.token)
vk_session_user = vk_api.VkApi(login=settings.vk_login,password=settings.vk_pass)

try:
    vk_session_user.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
vk_u = vk_session_user.get_api()

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

KEYBOARD_STEP_1 = {
    'one_time': False,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Понедельник😰',
        },
        'color': 'default'
    },
    {
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '2'}),
            'label': 'Вторник😓',
        },
        'color': 'default'
    }
    ],
    [{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Среда😱',
        },
        'color': 'default'
    },
    {
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '2'}),
            'label': 'Четверг🙄',
        },
        'color': 'default'
    }
    ],
    [{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Пятница😏',
        },
        'color': 'default'
    },
    {
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '2'}),
            'label': 'Суббота🤗',
        },
        'color': 'default'
    }
    ],
     [{
            'action': {
                'type': 'text',
                'payload': json.dumps({'buttons': '2'}),
                'label': 'Какой сегодня день?🤷‍♀️',
            },
            'color': 'primary'
        }
    ]
]
}


KEYBOARD_STEP_1_NEW = {
    'one_time': False,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Понедельник😰',
        },
        'color': 'default'
    },
    {
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '2'}),
            'label': 'Вторник😓',
        },
        'color': 'default'
    }
    ],
    [{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Среда😱',
        },
        'color': 'default'
    },
    {
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '2'}),
            'label': 'Четверг🙄',
        },
        'color': 'default'
    }
    ],
    [{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Пятница😏',
        },
        'color': 'default'
    },
    {
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '2'}),
            'label': 'Суббота🤗',
        },
        'color': 'default'
    }
    ],
    [{
            'action': {
                'type': 'text',
                'payload': json.dumps({'buttons': '1'}),
                'label': '#меню',
            },
            'color': 'negative'
        },
        {
            'action': {
                'type': 'text',
                'payload': json.dumps({'buttons': '2'}),
                'label': 'Сегодня🤷‍♀️',
            },
            'color': 'primary'
        },
        {
            'action': {
                'type': 'text',
                'payload': json.dumps({'buttons': '2'}),
                'label': '📸',
            },
            'color': 'positive'
        }]
]
}

KEYBOARD_STEP_2 = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': '09-641 (1)',
        },
        'color': 'default'
    },
    {
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '2'}),
            'label': '09-641 (2)',
        },
        'color': 'default'
    }
    ]
]
}

KEYBOARD_MENU = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Изменить подгруппу',
        },
        'color': 'primary'
    }
    ]
]
}

wb = openpyxl.load_workbook(filename = settings.excel)
sheet = wb['Бакалавриат']
sch = sched.schedule()
sch.setTimeAndNumOfLessons(sheet)
sch.setMondaySchedule(sheet)
sch.getMondaySchedule()
sch.getAllScheduleJSON()
def prepareNumOfDay(day):
    if day == "monday":
        return 0
    elif day == "tuesday":
        return 1
    elif day == "wednesday":
        return 2
    elif day == "thursday":
        return 3
    elif day == "friday":
        return 4
    elif day == "saturday":
        return 5
    else:
        return datetime.today().weekday()

def prepareDay(day,ru=False):
    if day == s.sat or day==5:
        return "saturday" if not ru else 'суббота'
    if day == s.mon or day==0:
        return "monday" if not ru else 'понедельник'
    if day == s.tue or day==1:
        return "tuesday" if not ru else 'вторник'
    if day == s.wed or day==2:
        return "wednesday" if not ru else 'среда'
    if day == s.thu or day==3:
        return "thursday" if not ru else 'четверг'
    if day == s.fri or day==4:
        return "friday" if not ru else 'пятница'
    if day == s.hz:
        return prepareDay(datetime.today().weekday(),ru=ru)
def genDate(day,stringFormat=False):
    today = datetime.today()
    todayWeekDay = datetime.today().weekday()
    if day < todayWeekDay:
        delta=6-day
        d = today + timedelta(days=delta)
        if stringFormat:
            return d.strftime("%d.%m.%Y")
        else:
            return d
    else:
        delta=day-todayWeekDay
        d = today + timedelta(days=delta)
        if stringFormat:
            return d.strftime("%d.%m.%Y")
        else:
            return d
def thisWeek(day):
    todayWeekDay = datetime.today().weekday()
    return False if day < todayWeekDay else True

try:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
       #Слушаем longpoll, если пришло сообщение то:
            if event.text == s.sat or event.text == s.thu or event.text == s.fri\
                    or event.text == s.mon or event.text == s.tue or event.text == s.wed or event.text==s.hz: #Если написали заданную фразу
                if event.from_user: #Если написали в ЛС
                    if not bd.select("SELECT * FROM user WHERE vk_id=?", (event.user_id,), isset=True):
                        messageText = "Выберите подгруппу, чтобы просмотреть расписание"
                        vk.messages.send(  # Отправляем сообщение
                            user_id=event.user_id,
                            message=messageText,
                            random_id=get_random_id(),
                            keyboard=json.dumps(KEYBOARD_STEP_2, ensure_ascii=False))
                    else:
                        group = bd.select("SELECT `group` FROM user WHERE vk_id=?", (event.user_id,))[0][0]
                        dateDay = genDate(prepareNumOfDay(prepareDay(event.text)),stringFormat=True)
                        chWeek = "ч/н" if sch.isChWeek(date=genDate(prepareNumOfDay(prepareDay(event.text)))) else "н/н"
                        thisWeekStr = "эта неделя" if thisWeek(prepareNumOfDay(prepareDay(event.text))) else "след. неделя"
                        doptext=''+prepareDay(event.text,ru=True)+' '+dateDay+" "+chWeek+'\n—————————————\n' if event.text==s.hz else prepareDay(event.text,ru=True)+' '+dateDay+" "+chWeek+'\n—————————————\n'
                        messageText=doptext+sch.getDaySheduleText(prepareDay(event.text),group=group)
                        vk.messages.send( #Отправляем сообщение
                            user_id=event.user_id,
                            message=messageText,
                            random_id = get_random_id(),
                            keyboard=json.dumps(KEYBOARD_STEP_1, ensure_ascii=False))

                elif event.from_chat: #Если написали в Беседе
                    vk.messages.send( #Отправляем собщение
                        chat_id=event.chat_id,
                        message='Ваш текст',
                        random_id=get_random_id())
            elif event.text == '09-641 (1)' or event.text == '09-641 (2)':
                group=1 if event.text == '09-641 (1)' else 2 #Деление на 2 группы
                if event.from_user:  # Если написали в ЛС
                    print("yes",vk_u.users.get(user_ids=event.user_id))
                    vk_name = vk_u.users.get(user_ids=event.user_id)[0]["first_name"]
                    if not bd.select("SELECT * FROM user WHERE vk_id=?",(event.user_id,),isset=True):

                        ins = bd.insert("INSERT INTO user('vk_id','vk_name','step','group') values(?,?,?,?)",(event.user_id,vk_name,1,group))
                        if ins:
                            messageText = "---Данные сохранены---\n"+vk_name+", теперь ты будешь видеть расписание для "+str(group)+" подгруппы.\n"+"Чтобы изменить свою группу наведи #меню."
                            vk.messages.send(  # Отправляем сообщение
                                user_id=event.user_id,
                                message=messageText,
                                random_id=get_random_id(),
                                keyboard=json.dumps(KEYBOARD_STEP_1, ensure_ascii=False))
                        else:
                            messageText = "Непредвиденная ошибка, попробуйте снова."
                            vk.messages.send(  # Отправляем сообщение
                                user_id=event.user_id,
                                message=messageText,
                                random_id=get_random_id(),
                                keyboard=json.dumps(KEYBOARD_STEP_2, ensure_ascii=False))
                    else:
                        upd = bd.update("""UPDATE user SET `group`=? WHERE vk_id=?""",(group,event.user_id))
                        if upd:
                            messageText = "---Данные обновлены---\n" + vk_name + ", теперь ты будешь видеть расписание для " + str(
                                group) + " подгруппы.\n" + "Чтобы изменить свою группу наведи #меню."
                            vk.messages.send(  # Отправляем сообщение
                                user_id=event.user_id,
                                message=messageText,
                                random_id=get_random_id(),
                                keyboard=json.dumps(KEYBOARD_STEP_1, ensure_ascii=False))
                        else:
                            messageText = "Непредвиденная ошибка, попробуйте снова."
                            vk.messages.send(  # Отправляем сообщение
                                user_id=event.user_id,
                                message=messageText,
                                random_id=get_random_id(),
                                keyboard=json.dumps(KEYBOARD_STEP_2, ensure_ascii=False))


            elif event.text == '#меню':
                if event.from_user:  # Если написали в ЛС
                    messageText = "Выберите нужный пункт меню."
                    vk.messages.send(  # Отправляем сообщение
                        user_id=event.user_id,
                        message=messageText,
                        random_id=get_random_id(),
                        keyboard=json.dumps(KEYBOARD_MENU, ensure_ascii=False))
            elif event.text == "Изменить подгруппу":
                if event.from_user:  # Если написали в ЛС
                    messageText = "Выберите нужный пункт."
                    vk.messages.send(  # Отправляем сообщение
                        user_id=event.user_id,
                        message=messageText,
                        random_id=get_random_id(),
                        keyboard=json.dumps(KEYBOARD_STEP_2, ensure_ascii=False))
            elif event.text == "Начать":
                if event.from_user:  # Если написали в ЛС
                    messageText = "Давайте начнём. Выберите свою подгруппу."
                    vk.messages.send(  # Отправляем сообщение
                        user_id=event.user_id,
                        message=messageText,
                        random_id=get_random_id(),
                        keyboard=json.dumps(KEYBOARD_STEP_2, ensure_ascii=False))
            elif event.text == "фото" or event.text == s.foto:
                path_photo = "1.jpg"
                #vk_api.VkUpload.photo_messages(path_photo)
                data = vk.photos.getMessagesUploadServer(user_id=event.user_id)

                upload_url = data["upload_url"]
                files = {'photo': open(path_photo, 'rb')}

                response = requests.post(upload_url, files=files)
                result = json.loads(response.text)

                uploadResult = vk.photos.saveMessagesPhoto(server=result["server"],
                                                              photo=result["photo"],
                                                              hash=result["hash"])
                #print(uploadResult,uploadResult[0]["owner_id"])
                attr="photo"+str(uploadResult[0]["owner_id"])+"_"+str(uploadResult[0]["id"])
                vk.messages.send(user_id=event.user_id,
                                    message="Расписание",
                                    random_id=get_random_id(),
                                    attachment=attr)

            elif event.text == "меню2":
                messageText='Меню 2'
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message=messageText,
                    random_id=get_random_id(),
                    keyboard=json.dumps(KEYBOARD_STEP_1_NEW, ensure_ascii=False))
            else:
                messageText='Выберите день недели'
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message=messageText,
                    random_id=get_random_id(),
                    keyboard=json.dumps(KEYBOARD_STEP_1, ensure_ascii=False))


except Exception:
    print("Error connection")






