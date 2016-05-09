#!/usr/bin/env python3
# coding=utf-8

import csv
import datetime

def get_date(str_date):
  return datetime.datetime.strptime(str_date, "%m/%d/%Y %H:%M:%S %p")

def main():
  with open("Crimes.csv") as cr:
    crime_reader = csv.DictReader(cr)
    
    crimes_2015 = {}
    
    for line in crime_reader:
      if get_date(line["Date"]).year == 2015:
        if line["Primary Type"] in crimes_2015:
          crimes_2015[line["Primary Type"]] += 1
        else:
          crimes_2015[line["Primary Type"]] = 1
    
    print(max(crimes_2015, key=crimes_2015.get))    

if __name__ == "__main__":
  main()