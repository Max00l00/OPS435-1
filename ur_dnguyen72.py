#!/usr/bin/env python3
"""
OPS435 Assignment 2 - Winter 2019
Program: ur_dnguyen72.py
Author: 'David Nguyen'
The python code in this file ur_dnguyen72.py is original work written by
'Student Name'. No code in this file is copied from any other source
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and violators
will be reported and appropriate action will be taken.
"""

import argparse
import os
import sys
import time


def get_login_rec():
    """
    The get_login_rec function will run when no file name is given but instead the
    string "last". The function will return a unformatted list from the filtered records
    of the the output from the last command.
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
    The read_login_rec takes one argument being a given log file name. The function will
    an unformatted list from the data from the the given file.
    """

    x = open(filelist, 'r')
    login_recs = x.readlines()
    x.close()
    return login_recs


def cal_daily_usage(subject, login_recs):
    """
    This function accepts two arguments, the first being the subject and the second being
    a list. The subject can be either a username or a ip address of a remote host. The
    function will then generate and return a daily usage report as well as the total daily usage.
    """



def cal_weekly_usage(subject, login_recs):


def cal_monthly_usage(subject, login_recs):



if __name__ == '__main__':

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
    parser.add_argument('-v', '--verbose', help='tune on unformatted_login_recs verbosity', action='store_true')
    args = parser.parse_args()

    unformatted_login_recs = []

    if "last" in args.filename:
        unformatted_login_recs.extend(get_login_rec())
    else:
        unformatted_login_recs.extend(read_login_rec(args.filename))

    if args.verbose:
        print('Files to be processed: ' + args.filename)
        print('Type of args for files' + type(args.filename))

        if args.list:
            print('processing usage report for the following:')
            print('reading login/logout record files ' + args.filename)
            print('Generating list for user')
        else:
            if args.rhost:
                print('usage report for remote host: ' + args.rhost)
            else:
                print('usage report for user: ' + args.user)
            print('usage report type:', args.type)
            print('processing usage report for the following:')
            print('reading login/logout record files', args.filename)

    if args.list:
        print(str(args.list) + ' list for ' + args.filename)
        print(len(str(args.list) + ' list for ' + args.filename) * '=')

    elif args.type:
        print(args.type + ' usage report for ' + args.user or args.rhost)
        print(len(args.type + ' usage report for ' + args.user or args.rhost) * '=')
        if args.type == 'daily':
            print('{:13} {:>13}'.format('Date', 'Usage in seconds'))
            print(cal_daily_usage(args.rhost or args.user, unformatted_login_recs))
        elif args.type == 'weekly':
            print('{:12} {:>12}'.format('Week #', 'Usage in seconds'))
            print(cal_monthly_usage(args.rhost or args.user, unformatted_login_recs))
        elif args.type == 'monthly':
            print('{:11} {:>11}'.format('Month', 'Usage in seconds'))
            print(cal_monthly_usage(args.rhost or args.user, unformatted_login_recs))
