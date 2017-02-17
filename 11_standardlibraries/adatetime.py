#!/usr/bin/python
import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks )

#Getting current time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

#Getting formatted time

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

'''
# displaying calendar
import calendar
    
cal = calendar.month(2015, 12)
print("Here is the calendar:")
print(cal)
'''

import time
import datetime

print ("Time in seconds since the epoch: %s" %time.time())
#print ("Current date and time: " , datetime.datetime.now())
#print ("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))


print ("Current year: ", datetime.date.today().strftime("%Y"))
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Week number of the year: ", datetime.date.today().strftime("%W"))
print ("Weekday of the week: ", datetime.date.today().strftime("%w"))
print ("Day of year: ", datetime.date.today().strftime("%j"))
print ("Day of the month : ", datetime.date.today().strftime("%d"))
print ("Day of week: ", datetime.date.today().strftime("%A"))















