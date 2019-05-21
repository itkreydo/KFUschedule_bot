# -*- coding: utf-8 -*-
import telebot
import cherrypy
import config
import sqlite3
import time as timer
from datetime import datetime, date, time
from telebot import types
import func,keyboards

bot = telebot.TeleBot(config.token)
stat = 0
chat = 0
timeSecStart = 0

conn = sqlite3.connect('sql.db')
c = conn.cursor()
c.execute("SELECT count(*) FROM users Where sername ='" + m.text + "'")
results = c.fetchall()