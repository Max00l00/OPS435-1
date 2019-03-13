#!/usr/bin/env python3
'''
OPS435 Assignment 1 - Winter 2019
Program: dnguyen72.py
Author: David Nguyen
The python code in this file (dnguyen72.py) is original work written by
David Nguyen. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import sys



def usage():
	'''
	The usage() function will output a string describing the proper usage of the script if the incorrect number of arguments are given.
	'''

	if ((len(sys.argv) != 4) and len(sys.argv) != 3):
		print(sys.argv[0] + '[--step] YYYYMMDD +/-n')
		exit()

def dbda(date,days): 
	'''
	The dbda() function takes two arguments; a date in "YYYYMMDD" format and a positive or negative interger.
	The function will add or subtract the amount of days corresponding to the interger from the given date and determine the new date. 

	Examples:
	dbda(20190101, 20)
	20190121
	'''

	if len(days) == 8:
		valid_date(days)

		day_counter = 0
		temp_day = days

		if date > days:

			while date > temp_day:
				temp_day = tomorrow(temp_day)
				day_counter = day_counter + 1
			
		elif temp_day > date:
			while date != temp_day:
				temp_day = yesterday(temp_day)
				day_counter = day_counter + 1

		print(day_counter)

	else:
		valid_date(date)

		year = int(date[0:4])
		month = int(date[4:6])
		day = int(date[6:])

		counter = int(days)
		new_date = date

		if counter > 0:
			while counter != 0:
				if sys.argv[1] == '--step':
					new_date = tomorrow(new_date)
					counter = counter - 1
					print(new_date)
				else:
					new_date = tomorrow(new_date)
					counter = counter - 1
		elif counter < 0:
			while counter != 0:
				if sys.argv[1] == '--step':
					new_date = yesterday(new_date)
					counter = counter + 1
					print(new_date)
				else:
					new_date = yesterday(new_date)
					counter = counter + 1
	if sys.argv[1] == '--step':
		print('',end='')
	else:
		print(new_date)

def tomorrow(date):
	'''
	The tomorrow() function will take a given date and return the date of the next day. 

	Example:
	tomorrow(20190101)
	20190102
	'''
	year = int(date[0:4])
	month = int(date[4:6])
	day = int(date[6:])
	temp_day = day + 1
	temp_month = month
	mon_max = days_in_mon(year)

    # If days go over 31
	if temp_day > mon_max[month]:
		temp_day = 1
		temp_month = month + 1

    # If month goes over max for year
	if temp_month > 12:
		temp_day = 1
		temp_month = 1
		year = year + 1

	next_day = str(year) + str(temp_month).zfill(2) + str(temp_day).zfill(2)
	return next_day

def yesterday(date):
	'''
	The yesterday() function will take a given date and return the date of the previous day.

	Example:
	yesterday(20190102)
	20190101
	'''

	year = int(date[0:4])
	month = int(date[4:6])
	day = int(date[6:])
	temp_day = day - 1
	temp_month = month
	mon_max = days_in_mon(year)

	# If day goes to 0
	if temp_day == 0:
		temp_day = mon_max[month]
		temp_month = month - 1

    # If month goes less than 1
	if temp_month == 0:
		temp_day = 31
		temp_month = 12
		year = year - 1

	previous_day = str(year) + str(temp_month).zfill(2) + str(temp_day).zfill(2)
	return previous_day

def valid_date(date):
	'''
	The valid_date() function will take a given date and determine if it is valid. If function will return True if valid, or give an error message if invalid.

	Examples:
	valid_date(2020247)
	Error: wrong date entered
	'''

	# Check if date format is valid
	if len(str(date)) != 8:
		print('Error: wrong date entered')
		exit()

	year = int(date[0:4])
	month = int(date[4:6]) 
	day = int(date[6:])

	# Check if month inputed is valid
	month_day = days_in_mon(year)
	if month not in month_day.keys():
		print('Error: wrong month entered')
		exit()

	# Check if day inputed is valid
	month_days_dictionary = days_in_mon(year)
	month_days = month_days_dictionary[month]

	if day not in range(1, month_days+1):
		print('Error: wrong day entered')
		exit()

def days_in_mon(year):
	'''
	The days_in_mon() function will take a given year and determine the maximum amount of days for each month in the given year.
	It will return a dictionary object containing the maximum days corresponding to each month of the given year.

	Examples:
	days_in_mon(2020)
	{1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	'''

	if leap_year(year) == 'TRUE':
		feb = 29
	else:
		feb = 28
	month_day = {1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return month_day


def leap_year(year):
	'''
	The leap_year() function will take a given year and determine whether it is a leap year or not.
	
	Examples:
	leap_year(2019)
	False
	'''

	# Determine if year given is a "leap year"
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				feb = 29
			else:
				feb = 28
		else:
			feb = 29
	else:
		feb = 28
	
	# Return TRUE or FALSE if leap year
	if feb == 28:
		return False
	else:
		return True

if __name__ == '__main__':
	usage()

	if sys.argv[1] == '--step':
		date = sys.argv[2]
		days = sys.argv[3]
	else:
		date = sys.argv[1]
		days = sys.argv[2]

	dbda(date, days)
