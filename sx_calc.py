# -*- coding: utf-8 -*-
"""SX Calc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rh2E2Rs6wgqd8-rN5h-wbHpJRij9BeZ3
"""

import datetime

today = datetime.date.today()

#Get when due
dateinput = input("Enter your when due date (YYYY-MM-DD): ")
year, month, day = map(int, dateinput.split('-'))
whendue = datetime.date(year, month, day)

#Get inspection interval
insp_amt = int(input("Enter days of inspection interval: "))

#Determine deviation
if insp_amt >= 90:
  deviation = 15
else:
  deviation = 3

#Calculate +- deviation from whendue
entersw = whendue - datetime.timedelta(days=deviation)
dropdead = whendue + datetime.timedelta(days=deviation)
nextdue = whendue + datetime.timedelta(days=insp_amt)


my_list = [entersw, today, whendue, nextdue, dropdead]
for ind in range(len(my_list)):
  my_list[ind] = my_list[ind].strftime("%d%b%Y")

print("ENTERS WINDOW:", my_list[0],", INITIATED:", my_list[1],", WHEN DUE:", my_list[2],", NEXT DUE:", my_list[3],", DROPS DEAD:", my_list[4],".")