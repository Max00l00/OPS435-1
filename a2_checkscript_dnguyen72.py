#!/usr/bin/env python3
"""
OPS435 Assignment 2 Checking Script
Program: a2_checkscript_dnguyen72.py
Author: 'David Nguyen'
The python code in this file a2_checkscript_dnguyen72.py is original work written by
David Nguyen. No code in this file is copied from any other source
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and violators
will be reported and appropriate action will be taken.
"""

import os
import sys


if __name__ == '__main__':
	os.system('clear')
	header = ('\r'+'==================================='+'\n'+'OPS435 Assignment 2 Checking Script'+
		'\n'+'==================================='+'\n')
	print(header, end='\r')
	if len(sys.argv) != 2:
		name = input('Please enter your senecaid: ')
	else:
		name = sys.argv[1]
	filename = 'ur_' + name + '.py'

	# Check if Assignment 2 file exists in current directory
	if os.path.isfile('./'+filename):
		print(header)
		print('Your assignment 2 script is not located in the current directory.'+'\n\n'+
			'Please move the assignent script to the same directory as the checking script and rerun','\n')
		exit()

	# Check for test results and test data
	if os.path.isfile('./a2_test_run_2_results.txt') == False:
		os.system('wget https://scs.senecac.on.ca/~raymond.chan/ops435/a2/a2_test_run_2_results.txt')
	if os.path.isfile('./a2_test_data_2') == False:
		os.system('wget https://scs.senecac.on.ca/~raymond.chan/ops435/a2/a2_test_data_2')







