# -*- coding: utf-8 -*-
import schedule
import time as timer
from datetime import datetime, date, time
def chet():
    ch = int(datetime.today().strftime("%U"))%2
    return ch
def day(d):
    dayy= ''
    if d == 1:
        dayy = 'Понедельник'
    elif d == 2:
        dayy = 'Вторник'
    elif d == 3:
        dayy = 'Среда'
    elif d == 4:
        dayy = 'Четверг'
    elif d == 5:
        dayy = 'Пятница'
    elif d == 6:
        dayy = 'Суббота'
    elif d == 7:
        dayy = 'Воскресенье'
    return dayy


def timetable(day,ch,gr1,gr2):
    table = ''
    if day == 1:
        if ch == 1:
            if gr1 == 1:
                if gr2 == 1:
                    table = schedule.mon111
                else:
                    table = schedule.mon112
            else:
                if gr2 == 1:
                    table = schedule.mon121
                else:
                    table = schedule.mon122
        else:
            if gr1 == 1:
                if gr2 == 1:
                    table = schedule.mon211
                else:
                    table = schedule.mon212
            else:
                if gr2 == 1:
                    table = schedule.mon221
                else:
                    table = schedule.mon222
    elif day == 2:
        if ch == 1:
            if gr1 == 1:
                table = schedule.tue11
            else:
                table = schedule.tue12
        else:
            if gr1 == 1:
                table = schedule.tue21
            else:
                table = schedule.tue22
    elif day == 3:
        if ch == 1:
            if gr1 == 1:
                if gr2 == 1:
                    table = schedule.wed111
                elif gr2 ==2:
                    table = schedule.wed112
                else:
                    table = schedule.wed113
            else:
                if gr2 == 1:
                    table = schedule.wed121
                elif gr2 ==2:
                    table = schedule.wed122
                else:
                    table = schedule.wed123
        else:
            if gr1 == 1:
                if gr2 == 1:
                    table = schedule.wed111
                elif gr2 ==2:
                    table = schedule.wed112
                else:
                    table = schedule.wed113
            else:
                if gr2 == 1:
                    table = schedule.wed121
                elif gr2 ==2:
                    table = schedule.wed122
                else:
                    table = schedule.wed123
    elif day == 4:
        if ch == 1:
            if gr1 == 1:
                table = schedule.thu11
            else:
                table = schedule.thu12
        else:
            if gr1 == 1:
                table = schedule.thu21
            else:
                table = schedule.thu22
    elif day == 5:
        if ch == 1:
            if gr1 == 1:
                table = schedule.fri11
            else:
                table = schedule.fri12
        else:
            if gr1 == 1:
                table = schedule.fri11
            else:
                table = schedule.fri12
    elif day == 6:
        if ch == 1:
            if gr1 == 1:
                table = schedule.sat1
            else:
                table = schedule.sat1
        else:
            if gr1 == 1:
                table = schedule.sat2
            else:
                table = schedule.sat2
    elif day == 7:
        table = schedule.sun
    return table
