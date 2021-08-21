'''4 > Write a Python program to print the calendar of a given month and year.'''
import calendar
m = int(input('Enter the month :'))
y = int(input('Enter the year :'))
print(calendar.month(y, m))