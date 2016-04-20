'''
В первой строке дано три числа, соответствующие некоторой 
дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, 
когда с момента исходной даты date пройдет число дней, равное days.
'''

#!/usr/bin/env python3
# coding=utf-8

import datetime
import sys

def read_time():
  reader = (tuple(map(int, line.split())) for line in sys.stdin)
  year, month, day = next(reader)
  
  return datetime.datetime(year, month, day)

def main():
  date = read_time()
  days_to_add = datetime.timedelta(int(input()))
  result = date + days_to_add
  print(result.year, result.month, result.day)

if __name__ == "__main__":
  main()