
#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import json
import functions
import classes
import pointListGenerator
import costFinder

granularity = 15

dtStart = sys.argv[1]
dtEnd = sys.argv[2]
txLocation = sys.argv[3]
txRRule = sys.argv[4]
temp = open("C:/wamp/www/mesa/python/temp1.json", "r")
blCalendars = json.loads(temp.read())
temp.close()
temp = open("C:/wamp/www/mesa/python/temp2.json", "r")
blSettings = json.loads(temp.read())
temp.close()

RRule = functions.parseRRule(txRRule)

priorities = functions.parsePriorities(blSettings)
originalEvent = classes.Event("blevent", {"blEvent":{"start_time":dtStart.replace(" ", "T")+"Z", "end_time":dtEnd.replace(" ", "T")+"Z", "location":txLocation, "travel_time":0}})
calendarSet = functions.construct_calendar_set(blCalendars)
pointList = pointListGenerator.construct_point_list(calendarSet, granularity, originalEvent, blSettings)

costOutput = costFinder.smallest_cost(pointList, priorities, originalEvent, granularity, txLocation, calendarSet)  
print (costOutput)
