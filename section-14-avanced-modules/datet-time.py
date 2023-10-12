import datetime
mytime = datetime.time(13, 20, 1, 20)

print(mytime.minute)

print(mytime.hour)

print(mytime)
print(mytime.microsecond)
print(type(mytime))

today = datetime.date.today()
print(today)

print(today.year)
print(today.month)

print(today.ctime())

mydatetime = datetime.datetime(2023, 10, 12, 11, 13, 50)

print(mydatetime)
mydatetime = mydatetime.replace(2022, 9)
print(mydatetime)

date1 = datetime.date(2023, 10, 20)
date2 = datetime.date(2022, 10, 20)
print(date1-date2)
result = date1-date2
print(result.days)
date3 = datetime.datetime(2023, 10, 20, 20)
date4 = datetime.datetime(2022, 10, 20, 8)

result2 = date3-date4
print(result2)
print(result2.seconds)
print(result2.total_seconds())
