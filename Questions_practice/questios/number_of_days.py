''' Calculate number of days by entering two dates '''

import datetime
from datetime import date

'''year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
date1 = datetime.date(year, month, day)

year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
date2 = datetime.date(year, month, day)

z = date2 - date1

print(z.days)'''


year = int(input('Enter a year: '))
month =int(input('Enter a month: '))
day = int(input('Enter a day: '))
x = datetime.date(year, month,day)

year = int(input('Enter a year: '))
month =int(input('Enter a month: '))
day = int(input('Enter a day: '))
y = datetime.date(year, month,day)
z = y - x
print(z.days)