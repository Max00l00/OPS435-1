#!/usr/bin/env python3
'''
OPS435 Assignment 2 - Winter 2019
Program: ur_[dnguyen72].py
Author: "David Nguyen"
The python code in this file ur_[dguyen72].py is original work written by
"Student Name". No code in this file is copied from any other source
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and violators
will be reported and appropriate action will be taken.
'''

import argparse
import os
import sys
import time

def get_login_rec():
    """
    Get records from the last command, filter out the unwanted records,
    and add filtered record to list (login_recs).
    """

    last = 'last -Fiw'
    x = os.popen(last)
    results = x.readlines()
    x.close()
    login_recs = []
    for item in results:
        if len(item.split()) == 15:
            login_recs.append(item)
    return login_recs


def read_login_rec(filelist):
    """
    Get records from given filelist, open and read each file from the filelist,
    filter out the unwanted records and add filtered record to list (login_recs)
    """

    x = open(filelist, 'r')
    login_recs = x.readlines()

    return login_recs


if __name__ == '__main__':
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)
    '''

    # Arguments

    parser = argparse.ArgumentParser(description='Usage Report based on the last command',
                                     epilog='\nCopyright 2018 - David Nguyen')
    parser.add_argument('filename', metavar='F', nargs='*', default='empty', help='list of files to be processed')
    parser.add_argument('-l', '--list', choices=['user', 'host'],
                        help='generates user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost', metavar='RHOST', help='usage report for the given remote host IP')
    parser.add_argument('-t', '--type', choices=['daily', 'weekly', 'monthly'],
                        help='type of report: daily, weekly, and monthly')
    parser.add_argument('-u', '--user', help='usage report for the given user name')
    parser.add_argument('-v', '--verbose', help='tune on output verbosity', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        print('Files to be processed: ' + args.filename)
        print('Type of args for files' + type(args.filename))

        if args.list:
            print('processing usage report for the following:')
            print('reading login/logout record files ' + args.filename)
            print('Generating list for user')

        else:
            print('usage report for user: ' + subject)
