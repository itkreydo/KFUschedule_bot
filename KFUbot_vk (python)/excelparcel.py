import openpyxl
import modules.settings as settings
import modules.scheduleClass as sched


wb = openpyxl.load_workbook(filename = settings.excel)
sheet = wb['Бакалавриат']
print(sheet['A1'].value)
i=sheet['A50'].font.color.rgb #Green Color

print(i)


sch = sched.schedule()
sch.setTimeAndNumOfLessons(sheet)
sch.setMondaySchedule(sheet)
sch.getMondaySchedule()
sch.getDaySheduleText("monday")
sch.setNapArray(sheet)
print(sch.getDaySchedule("monday")[1]["first_nn"])


print()