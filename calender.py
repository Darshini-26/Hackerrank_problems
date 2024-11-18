import calendar
month,date,year= list(map(int,input().split()))
num=calendar.weekday(year,month,date)
print(calendar.day_name[num].upper())
