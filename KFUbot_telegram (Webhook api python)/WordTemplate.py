from docxtpl import DocxTemplate

class soc:
    fio=''
    pasSer=''
    pasNum=''
    pasVidan=''
    pasCod =''
    pD =''
    pM=''
    pY=''
    regAdress=''
    LiveAdress=''
    BirthAdress=''
    dateOfBirth=''
    phone=''
    inn =''
    strah =''
    index =''
    Init = ''
    def Initial(self):
        self.Init = self.fio.split(" ")
        self.Init = self.Init[0] + " " + self.Init[1][0] + "." + self.Init[2][0] + "."
        print(self.Init)
def wordWriteDataFunction(i,text,socc):
    res={'i':1,'msg':'0'}
    msg =0
    if i == 1:
        socc.fio = text
        msg='Введи серию паспорта (****)'
    if i == 2:
        socc.pasSer = text
        msg = 'Введи номер паспорта (******)'
    if i == 3:
        socc.pasNum = text
        msg = 'Кем выдан'
    if i == 4:
        print(socc.fio,socc.pasSer)
        socc.pasVidan = text
        msg = 'Код подразделения(***-***)'
    if i == 5:
        socc.pasCod = text
        msg = 'Дата выдачи (**.**.****)'
    if i == 6:
        p = text.split(".")
        socc.pD = p[0]
        socc.pM = p[1]
        socc.pY = p[2]
        msg = 'Адрес регистрации'
    if i == 7:
        socc.regAdress = text
        msg = 'Адрес проживания'
    if i == 8:
        socc.LiveAdress = text
        msg = 'Место рождения'
    if i == 9:
        socc.BirthAdress = text
        msg = 'Дата рождения (**.**.****)'
    if i == 10:
        socc.dateOfBirth = text
        msg = 'Телефон (начиная с 8)'
    if i == 11:
        socc.phone = text
        msg = 'ИНН'
    if i == 12:
        socc.inn = text
        msg = 'Страховое свид-во (без пробелов и тире)'
    if i == 13:
        socc.strah = text
        msg = 'Индекс места жительства'
    if i == 14:
        socc.index = text
        msg = 'Обработка данных...'
        wordWriteFunction(socc)

    res['msg']=msg
    res['i']=i+1
    res['data']=socc
    return res


def wordWriteFunction(soc):
    soc.Initial()
    context = { 'fio' : soc.fio ,
                'pasSer' : soc.pasSer, 'pasNum' : soc.pasNum,
                'pasVidan' : soc.pasVidan,
                'regAdress' : soc.regAdress,
                'LiveAdress' : soc.LiveAdress,
                'BirthAdress' : soc.BirthAdress,
                'dateOfBirth' : soc.dateOfBirth,
                'inn' : soc.inn,
                'phone' : soc.phone,
                'pD' : soc.pD,
                'pM' : soc.pM,
                'pY' : soc.pY,
                'pasCod' : soc.pasCod,
                's1': soc.pasSer[0],
                's2': soc.pasSer[1],
                's3': soc.pasSer[2],
                's4': soc.pasSer[3],
                'n1': soc.pasNum[0],
                'n2': soc.pasNum[1],
                'n3': soc.pasNum[2],
                'n4': soc.pasNum[3],
                'n5': soc.pasNum[4],
                'n6': soc.pasNum[5],
                'y1': soc.pY[0],
                'y2': soc.pY[1],
                'y3': soc.pY[2],
                'y4': soc.pY[3],
                'i1':soc.inn[0],
                'i2':soc.inn[1],
                'i3':soc.inn[2],
                'i4':soc.inn[3],
                'i5':soc.inn[4],
                'i6':soc.inn[5],
                'i7':soc.inn[6],
                'i8':soc.inn[7],
                'i9':soc.inn[8],
                'i10':soc.inn[9],
                'i11':soc.inn[10],
                'i12':soc.inn[11],
                'v1':soc.strah[0],
                'v2':soc.strah[1],
                'v3':soc.strah[2],
                'v4':soc.strah[3],
                'v5':soc.strah[4],
                'v6':soc.strah[5],
                'v7':soc.strah[6],
                'v8':soc.strah[7],
                'v9':soc.strah[8],
                'v10':soc.strah[9],
                'v11':soc.strah[10],
                'p1':soc.phone[0],
                'p2':soc.phone[1],
                'p3':soc.phone[2],
                'p4':soc.phone[3],
                'p5':soc.phone[4],
                'p6':soc.phone[5],
                'p7':soc.phone[6],
                'p8':soc.phone[7],
                'p9':soc.phone[8],
                'p10':soc.phone[9],
                'p11':soc.phone[10],
                'd1': soc.dateOfBirth[0],
                'd2': soc.dateOfBirth[1],
                'd3': soc.dateOfBirth[3],
                'd4': soc.dateOfBirth[4],
                'd5': soc.dateOfBirth[6],
                'd6': soc.dateOfBirth[7],
                'd7': soc.dateOfBirth[8],
                'd8': soc.dateOfBirth[9],
                'index': soc.index,
                'Init' :soc.Init
                }

    doc = DocxTemplate("/home/scheduleKFU/socPit/dogovor.docx")
    doc.render(context)
    doc.save("/home/scheduleKFU/socPit/gotovo/dogovor.docx")

    doc = DocxTemplate("/home/scheduleKFU/socPit/soglasie.docx")
    doc.render(context)
    doc.save("/home/scheduleKFU/socPit/gotovo/Soglasie.docx")

    doc = DocxTemplate("/home/scheduleKFU/socPit/zayavlenierasp.docx")
    doc.render(context)
    doc.save("/home/scheduleKFU/socPit/gotovo/ZayavlenieRaz.docx")

    doc = DocxTemplate("/home/scheduleKFU/socPit/OprosAnketa.docx")
    doc.render(context)
    doc.save("/home/scheduleKFU/socPit/gotovo/OprosAnketa.docx")

    doc = DocxTemplate("/home/scheduleKFU/socPit/DopAnketa.docx")
    doc.render(context)
    doc.save("/home/scheduleKFU/socPit/gotovo/DopAnketa.docx")
    doc = DocxTemplate("/home/scheduleKFU/socPit/ZayavlenieNaPit.docx")
    doc.render(context)
    doc.save("/home/scheduleKFU/socPit/gotovo/ZayavlenieNaPit.docx")
