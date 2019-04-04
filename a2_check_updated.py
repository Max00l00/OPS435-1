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
import subprocess


if __name__ == '__main__':
	os.system('clear')
	header = ('\r'+'==================================='+'\n'+'OPS435 Assignment 2 Checking Script'+
		'\n'+'==================================='+'\n\n')
	print(header, end='\r')
	if len(sys.argv) != 2:
		name = input('Please enter your senecaid: ')
	else:
		name = sys.argv[1]
	filename = 'ur_' + name + '.py'

	################################################################

	# Check if Assignment 2 file exists in current directory
	if os.path.isfile('./'+filename) == False:
		print('\n'+'Your assignment 2 script is not located in the current directory.'+'\n\n'+
			'Please move the assignent script to the same directory as the checking script and rerun','\n')
		exit()

	# Check for test results and test data
	if os.path.isfile('./a2_test_run_2_results.txt') == False:
		os.system('wget https://scs.senecac.on.ca/~raymond.chan/ops435/a2/a2_test_run_2_results.txt')
	if os.path.isfile('./a2_test_data_2') == False:
		os.system('wget https://scs.senecac.on.ca/~raymond.chan/ops435/a2/a2_test_data_2')
	test_file = 'a2_test_data_2'
	test_results = 'a2_test_run_2_results.txt'

	# Extract Test results 
	f = open(test_results, 'r')
	results = f.readlines()
	f.close()
	del results[0:57] # deleting un-needed text
	#os.system('rm -r ' + test_results) # remove file after extracting
	
	# Extract commands and output from test results
	cmd_output = {}
	for line in results:
		if line.startswith('+'):
			command = line.replace('+ ./ur.py ', 'python3 ' + filename + ' ')
			cmd_output[command] = []
		else:
			cmd_output[command].append(line.strip('\n'))

	# Save user answer's script output to dictionary\
	user_answer = {}
	for cmd in cmd_output.keys():
		p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
		get_output = p.communicate()[0].decode('utf-8').strip('\n')
		user_answer[cmd] = get_output.split('\n')

	# Output Marks and compare
	total_marks = 0								# Total marks recieved for line comparison
	total_lines = 0								# Total lines to compare									
	for cmd in user_answer:
		user_output = cmd_output[cmd]			# All lines from user output for given cmd
		answer_output = user_answer[cmd]		# All liens of output from answer key for cmd
		test_marks = 0							# Total marks earned for specific test
		total_lines += len(answer_output)
		print('{:^111}'.format('Testing: '+cmd))
		print("{:<55s}{:>55s}".format("EXPECTED", "GIVEN"))
		print(len("{:<55s}{:>55s}".format("EXPECTED", "GIVEN"))*'=')
		for line in range(len(answer_output)):
			print('{:<1}{:<55}'.format(answer_output[line], user_output[line]))
			#print('========','EXPECTED','========')
			# print('\n'.join(cmd_output[cmd]))	
			#print('=========','GIVEN','==========')
			# print('\n'.join(user_answer[cmd])+'\n')
			if answer_output[line] == user_output[line]:
				total_marks += 1
				test_marks += 1
		print('\n'+'Total marks recieved for test: '+'['+str(test_marks)+'/'+str(len(answer_output))+']'+'\n\n')
			#print('\n\n')

	# Output final scores

	final_mark = total_marks / int(total_lines)*100 # Calculate final result as percentage
	print('Total marks recieved: '+'[' + str(total_marks)+'/'+str(total_lines)+']')
	print('Final mark for script: '+str(round(final_mark))+'%')


		

