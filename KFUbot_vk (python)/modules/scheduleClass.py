import openpyxl
import json
from datetime import datetime, date, time
def getValueWithMergeLookup(sheet, cell):
    #idx = cell.coordinate
    idx = cell
    for range_ in sheet.merged_cell_ranges:
        merged_cells = list(openpyxl.utils.cell.rows_from_range(str(range_)))
        for row in merged_cells:
            if idx in row:
                # If this is a merged cell,
                # return  the first cell of the merge range
                return sheet[merged_cells[0][0]].value
    return sheet[idx].value
class schedule:
    xlsx=''
    group = ''
    nap = ''
    monday = ''
    numOfLessonsInDay = []
    numOfDays = 6
    startCellForStart = 6
    scheduleAll={}
    scheduleJSON =''
    dateStartLessons=''
    FizRaTitle = 'УНИКС'
    timeLesson=[]
    infoKources={}
    def __init__(self,xlsx=False):
        """Constructor"""
        pass
        self.xlsx=xlsx
        self.dateStartLessons=date(2019, 2, 7)
        self.timeLessonFizRa=["8.00-9.30","10.00-11.30","12.00-13.30","14.00-15.30","16.00-17.30","16.00-17.30","16.00-17.30"]
    def setNap(self,xlsx):
        self.nap=xlsx['CB4'].value
    def setGroup(self,xlsx):
        self.nap=xlsx['CB5'].value
    def setMondaySchedule(self,xlsx):
        startIndex = self.startCellForStart
        for i in range(self.numOfDays):
            print("----------NEW DAY-----------",i)
            daySch={}
            for j in range(self.numOfLessonsInDay[i]):
                kod = startIndex + j*2
                a=getValueWithMergeLookup(xlsx,'CB'+str(kod))
                stroka = {'first_nn': {'group1': getValueWithMergeLookup(xlsx,'CB'+str(kod)), 'group2': getValueWithMergeLookup(xlsx,'CC'+str(kod))},
                      'second_cn': {'group1': getValueWithMergeLookup(xlsx,'CB'+str(kod+1)), 'group2': getValueWithMergeLookup(xlsx,'CC'+str(kod+1))}}
                daySch[j]=stroka
            self.scheduleAll[self.numToDay(i)]=daySch
            startIndex = kod+3#next day start
    def getAllScheduleJSON(self):
        print(self.scheduleAll);
    def getMondaySchedule(self):
        self.scheduleJSON = json.dumps(self.scheduleAll,ensure_ascii=False)
        #print(self.scheduleJSON)
    def setTimeAndNumOfLessons(self,xlsx):
        startindex=self.startCellForStart
        dni = ["пн","вт","ср","чт","пт","сб","."]
        for i in range(len(dni)-1):
            status = True
            countLesson=0
            while status:
                if (xlsx["B"+str(startindex)].value in dni):
                    status=False
                    startindex+=1
                else:
                    if (i == 0): self.timeLesson.append(xlsx["B"+str(startindex)].value)
                    startindex+=2
                    countLesson += 1
            self.numOfLessonsInDay.append(countLesson)
        print(self.timeLesson)
    def setNapArray(self,xlsx):
        koursNapRow = '4'

        self.infoKources = {}
        kources = ['0 курс','1 курс','2 курс','3 курс','4 курс',None]
        info = {}
        infoSubGroup =[]
        infoNap=[]
        infoNapKey={}
        lastValue=0
        infokourse={}
        stat=True
        for col in xlsx.iter_cols():
            colVal = getValueWithMergeLookup(xlsx, col[3].coordinate)
            colSubGroupVal = getValueWithMergeLookup(xlsx, col[4].coordinate)
            if colVal in kources:
                if stat is True:
                    stat=False
                    infoNapKey.update({lastValue: infoSubGroup})
                    infokourse[kources[kources.index(colVal)-1]] = infoNapKey
                    infoNapKey = {}
                    lastValue=0
                    infoSubGroup=[]
                    print(colVal)
            else:
                if (lastValue!=colVal):
                    infoNap.append(lastValue)
                    infoNapKey.update({lastValue: infoSubGroup})
                    infoSubGroup=[]
                    infoSubGroup.append(colSubGroupVal)
                    lastValue=colVal
                else:
                    infoSubGroup.append(colSubGroupVal)
                stat = True
        self.infoKources =infokourse
        self.formatInfoKources()
        print(self.infoKources)
    def formatInfoKources(self):
        for kurs in self.infoKources:
            #kurs.pop(0,None)
            for nap in kurs:
                print()
            #print(getValueWithMergeLookup(xlsx, col[3].coordinate))
    def getTimeOfLesson(self,i):
        return self.timeLesson[i]
    def getDaySchedule(self,day):
        return self.scheduleAll[day]
    def isChWeek(self,date=False):
        if date==False:
            date=datetime.today()
        date = datetime.isocalendar(date)[1]
        deltaWeekFromStart=date-datetime.isocalendar(self.dateStartLessons)[1]
        if ((deltaWeekFromStart + 1) % 2==0):
            return True
        else:
            return False

    def getDaySheduleText(self,day,group=1):
        sch = self.scheduleAll[day]
        s = ''
        for i in range(len(sch)):
            chSch = sch[i]["second_ch"] if self.isChWeek() else sch[i]["first_nn"]
            groupSch = chSch["group"+str(group)] if chSch["group"+str(group)] != "" else " — "
            #print(chSch)
            f = groupSch.find(self.FizRaTitle)
            time = self.getTimeOfLesson(i) if groupSch.find(self.FizRaTitle) == -1 else self.timeLessonFizRa[i]
            s+=self.numToEmoji(i+1)+time+groupSch+'\n'
        return s
    def numToEmoji(self,num):
        emodzi_num=['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
        return emodzi_num[num]

    def numToDay(self,num):
        if num==0:
            return "monday"
        elif num ==1:
            return "tuesday"
        elif num ==2:
            return "wednesday"
        elif num ==3:
            return "thursday"
        elif num ==4:
            return "friday"
        elif num ==5:
            return "saturday"
        elif num ==6:
            return "sunday"



