# -*- coding: utf-8 -*-
import telebot
import cherrypy
import config
import sqlite3
import time as timer
from datetime import datetime, date, time
from telebot import types
import func,keyboards
import time as times
import WordTemplate

# key value vor soc pit
conn = sqlite3.connect('/home/scheduleKFU/sql.db')
c = conn.cursor()
c.execute("SELECT count(*) FROM users Where chat_id != 0")
count = c.fetchall()
c.execute("SELECT * FROM users Where chat_id != 0")
results = c.fetchall()
d = {}
for i in range(count[0][0]):
    d[results[i][4]] = 0
print('k/v: ',d)
usersData = {}
for i in range(count[0][0]):
    usersData[results[i][4]] = WordTemplate.soc()
# key value vor soc pit

bot = telebot.TeleBot(config.token)
stat = 0
chat = 0
timeSecStart = 0
class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(commands=["relogin"])
def Changename(m):
    bot.send_message(m.chat.id,
                     'Хочешь посмотреть расписание у кого-то другого?😉 \nВведи фамилию')

@bot.message_handler(commands=["soc"])
def Changename(m):
    bot.send_message(m.chat.id,
                     '🍔Вы включили режим заполнения соц. питания\nТебе нужно будет ответить на 14 простых вопросов\nИтак, приступим')
    bot.send_message(m.chat.id,
                     'Введи ФИО')
    d[m.chat.id] = 1

@bot.message_handler(commands=["say"])
def Changename(m):
    if (m.chat.id==422105423):
        bot.send_message(m.chat.id, 'Твоё сообщение отправлено всем участникам')
        i=0
        conn = sqlite3.connect('/home/scheduleKFU/sql.db')
        c = conn.cursor()
        c.execute("SELECT count(*) FROM users Where chat_id != 0")
        count = c.fetchall()
        c.execute("SELECT * FROM users Where chat_id != 0")
        results = c.fetchall()
        print(results)
        while i < count[0][0]:
            bot.send_message(results[i][4],'❗️Инфа от старосты❗️\n'+m.text[4:len(m.text)])
            print(results[i][1])
            times.sleep(3)
            i+=1
    else:
        bot.send_message(m.chat.id, 'У тебя нет доступа к этой команде')


@bot.message_handler(commands=["update"])
def Changename(m):
    if (m.chat.id == 260905393):
        bot.send_message(m.chat.id,'Info sended')
        i=0
        conn = sqlite3.connect('/home/scheduleKFU/sql.db')
        c = conn.cursor()
        c.execute("SELECT count(*) FROM users Where chat_id != 0")
        count = c.fetchall()
        c.execute("SELECT * FROM users Where chat_id != 0")
        results = c.fetchall()
        print(results)
        while i < count[0][0]:
            bot.send_message(results[i][4],'🔅 Обновление 🔅\n'+m.text[7:len(m.text)])
            print(results[i][1])
            times.sleep(3)
            i+=1
    else:
        bot.send_message(m.chat.id, 'У тебя нет доступа к этой команде')

@bot.message_handler(commands=["info7"])
def Changename(m):
    bot.send_message(m.chat.id,'Info sended')
    i=0
    conn = sqlite3.connect('/home/scheduleKFU/sql.db')
    c = conn.cursor()
    c.execute("SELECT count(*) FROM users Where chat_id != 0")
    count = c.fetchall()
    c.execute("SELECT * FROM users Where chat_id != 0")
    results = c.fetchall()
    print(results)
    while i < count[0][0]:
        bot.send_message(results[i][4],'⚠️Информация⚠️\n'+m.text[6:len(m.text)])
        print(results[i][1])
        times.sleep(3)
        i+=1


@bot.message_handler(commands=["menu"])
def Changename(m):
    bot.send_message(m.chat.id, '🔅Меню🔅', reply_markup=keyboards.keyboardMenu)
@bot.message_handler(commands=["stop"])
def Changename(m):
    bot.send_message(m.chat.id, 'Вы отключили режим заполнения документов. Добро пожаловать в обычную жизнь👍', reply_markup=keyboards.keyboardMenu)
    d[m.chat.id] = 0



@bot.message_handler(commands=["start"])
def GroupChoose(m):
    global stat
    global chat
    global timeSecStart
    bot.send_message(m.chat.id,
                     'Привет, студент🖐 \nЯ подскажу тебе расписание на любой день и буду присылать важную информацию) \nОбновления в версии 2.0: \n🎧 - так обозначаются лекции \n🔅Добавлена кнопка "Фотка Расписания📸"\n')
    conn = sqlite3.connect('/home/scheduleKFU/sql.db')
    c = conn.cursor()
    c.execute("SELECT count(*) FROM users Where chat_id = " + str(m.chat.id))
    results = c.fetchall()
    print('New user /start')
    if (results[0][0] == 0):
        bot.send_message(m.chat.id, 'Введи свою фамилию')
    else:
        c.execute("SELECT * FROM users Where chat_id = " + str(m.chat.id))
        results = c.fetchall()
        bot.send_message(m.chat.id, 'Добро пожаловать, ' + results[0][1])
        bot.send_message(m.chat.id, 'Ты в ' + str(results[0][2]) + ' группе')
        bot.send_message(m.chat.id, 'Выбери день', reply_markup=keyboards.keyboard)


# Хэндлер на все текстовые сообщения
@bot.message_handler(func=lambda message: True, content_types=['text'])
def scheduleChoose(m):
    global stat
    global chat
    conn = sqlite3.connect('/home/scheduleKFU/sql.db')
    c = conn.cursor()
    c.execute("SELECT count(*) FROM users Where chat_id = " + str(m.chat.id))
    results = c.fetchall()
    print('new message')
    print(results[0][0])
    if (results[0][0] == 0):
        c.execute("SELECT count(*) FROM users Where sername ='" + m.text + "'")
        results = c.fetchall()
        if results[0][0] == 0:
            bot.send_message(m.chat.id,
                             'Очень жаль, но такого студента у нас нет. \nВозможно ты ошибся при вводе фамилии, попробуй ещё раз. /start')
            return
        c.execute("SELECT * FROM users Where sername ='" + m.text + "'")
        results = c.fetchall()
        c.execute("UPDATE users SET chat_id = ? WHERE sername = ? ", (m.chat.id, m.text))
        conn.commit()
        bot.send_message(m.chat.id, 'Добро пожаловать, ' + m.text)
        bot.send_message(m.chat.id, 'Ты в ' + str(results[0][2]) + ' группе')
        bot.send_message(m.chat.id, 'Выбери день', reply_markup=keyboards.keyboard)
        print('зареган '+m.text)
    else:
        print('est')
        c.execute("SELECT * FROM users Where chat_id = " + str(m.chat.id))
        results = c.fetchall()
        print(results)
        #soc pit
        if d[m.chat.id]!=0:

            res=WordTemplate.wordWriteDataFunction(d[m.chat.id],m.text,usersData[m.chat.id])
            usersData[m.chat.id]=res['data']
            d[m.chat.id] = res['i']
            print(usersData[m.chat.id].fio)
            bot.send_message(m.chat.id, res['msg'])
            if (d[m.chat.id] == 15):
                d[m.chat.id] =0
                doc1 = open('/home/scheduleKFU/socPit/gotovo/ZayavlenieNaPit.docx', 'rb')
                doc2 = open('/home/scheduleKFU/socPit/gotovo/dogovor.docx', 'rb')
                doc3 = open('/home/scheduleKFU/socPit/gotovo/Soglasie.docx', 'rb')
                doc4 = open('/home/scheduleKFU/socPit/gotovo/ZayavlenieRaz.docx', 'rb')
                doc5 = open('/home/scheduleKFU/socPit/gotovo/OprosAnketa.docx', 'rb')
                doc6 = open('/home/scheduleKFU/socPit/gotovo/DopAnketa.docx', 'rb')
                bot.send_document(m.chat.id, doc1)
                bot.send_document(m.chat.id, doc2)
                bot.send_document(m.chat.id, doc3)
                bot.send_document(m.chat.id, doc4)
                bot.send_document(m.chat.id, doc5)
                bot.send_document(m.chat.id, doc6)
                doc1.close()
                doc2.close()
                doc3.close()
                doc4.close()
                doc5.close()
                doc6.close()
                bot.send_message(260905393, "🍔 "+usersData[m.chat.id].fio)
                bot.send_message(m.chat.id,
                                 '✨Поздравляю!\n Только что вы заполнили все документы на соц. питание.\nНаслаждайтесь едой, пока на вас оформляется кредит:)')

            return
        #soc pit

        if m.text == 'Понедельник📚':
            bot.send_message(m.chat.id, func.timetable(1, func.chet(), results[0][2],results[0][3]), reply_markup=keyboards.keyboard)
            print('выбрал понедельник')
        elif m.text == 'Вторник📚':
            bot.send_message(m.chat.id, func.timetable(2, func.chet(), results[0][2],results[0][3]), reply_markup=keyboards.keyboard)
            print('выбрал вторник')
        elif m.text == 'Среда📚':
            bot.send_message(m.chat.id, func.timetable(3, func.chet(), results[0][2],results[0][3]), reply_markup=keyboards.keyboard)
            print('выбрал среду')
        elif m.text == 'Пятница📚':
            bot.send_message(m.chat.id, func.timetable(5, func.chet(), results[0][2],results[0][3]), reply_markup=keyboards.keyboard)
            print('выбрал пятницу')
        elif m.text == 'Четверг📚':
            bot.send_message(m.chat.id, func.timetable(4, func.chet(), results[0][2],results[0][3]), reply_markup=keyboards.keyboard)
            print('выбрал четверг')
        elif m.text == 'Суббота📚':
            bot.send_message(m.chat.id, func.timetable(6, func.chet(), results[0][2],results[0][3]), reply_markup=keyboards.keyboard)
            print('выбрал субботу')
        elif m.text == 'Хз какой день, куда мне идти?🤷‍♂':
            print('выбрал хз какой день')
            if (func.chet()==1):
                chetNed='н/н'
            else:
                chetNed = 'ч/н'
            bot.send_message(m.chat.id, 'Сегодня ' + func.day(datetime.today().isoweekday())+' '+chetNed, reply_markup=keyboards.keyboard)
            bot.send_message(m.chat.id,
                             func.timetable(datetime.today().isoweekday(), func.chet(), results[0][2],results[0][3]),
                             reply_markup=keyboards.keyboard)
        elif m.text == 'Фотка расписания📸':
            photo = '/home/scheduleKFU/sch.jpg'
            print('photo send button')
            bot.send_photo(m.chat.id, open(photo, 'rb'))
        elif m.text == 'Документы Соц. Пит.🍔':
            bot.send_message(m.chat.id,'Вы включили режим заполнения соц. питания🍔\n Тебе нужно будет ответить на 14 простых вопросов\nВведите /stop, если передумали заполнять документы или допустили ошибку.\nИтак, приступим')
            bot.send_message(m.chat.id,'Введи ФИО')
            d[m.chat.id] = 1
        elif m.text == 'Расписание 🗒':
            bot.send_message(m.chat.id,'Выбери день', reply_markup=keyboards.keyboard)
        elif m.text == 'Secret':
            bot.send_message(m.chat.id,'Это секрет, и никто не знает что там, и когда это заработает😅', reply_markup=keyboards.keyboard)
        else:
            c.execute("SELECT * FROM users Where chat_id = " + str(m.chat.id))
            results = c.fetchall()
            bot.send_message(422105423, '🔅 '+results[0][1]+': '+m.text)


# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()
 # Ставим заново вебхук
bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH,
                certificate=open(config.WEBHOOK_SSL_CERT, 'r'))
# Указываем настройки сервера CherryPy
cherrypy.config.update({
    'server.socket_host': config.WEBHOOK_LISTEN,
    'server.socket_port': config.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': config.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': config.WEBHOOK_SSL_PRIV
})
 # Собственно, запуск!
cherrypy.quickstart(WebhookServer(), config.WEBHOOK_URL_PATH, {'/': {}})