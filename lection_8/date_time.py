from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import locale

d1 = date(2019, 3, 12)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)


t1 = time(23, 10, 59)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)


print(date.today())

print(date.max)
print(date.min)
print(time.max)
print(time.min)


dt = datetime(2019, 3, 12, 15, 17)
print(dt)
print(dt.date().year)
print(dt.time().hour)

print(dt.max)
print(dt.min)


now = datetime.now()
print(now)

new_dt = now.replace(year=2018)
print(new_dt)


dt_2 = datetime.strptime('30/08/2018', '%d/%m/%Y')
print(dt_2)

dt_3 = datetime.strptime('06-28-2018 10:40', '%m-%d-%Y %H:%M')
print(dt_3)

locale.setlocale(locale.LC_ALL, '')

now = datetime.now()
print(now.strftime('%Y-%m-%d (%a)'))
print(now.strftime('%Y %B %d число (%A)'))


delta1 = timedelta(days=3, hours=2, minutes=10)
print(delta1)
delta2 = timedelta(days=2, hours=1, minutes=5)

print(delta1-delta2)
print(delta2-delta1)


my_birthday = date(1992, 8, 12)
delta = date.today() - my_birthday
print(type(delta))

my_age = int(delta.days/365)
print(my_age)