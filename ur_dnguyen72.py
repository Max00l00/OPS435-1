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

import sys
import argparse
import time
import os

def get_login_rec():

    '''
    Get records from the last command, filter out the unwanted records, and add filtered record to list (login_recs).
    '''

    login_recs = []
    last_command = last -Fiw

    return login_recs


def read_login_rec(filelist):
    ''' docstring for this function
    get records from given filelist
    open and read each file from the filelist
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    [put your python code
    for this function here]
    return login_rec


def cal_daily_usage(subject, login_recs):
    ''' docstring for this function
    generate daily usage report for the given
    subject (user or remote host)'''
    [put your python code
    for this function here]
    return daily_usage


def cal_weekly_usage(subject, login_recs):
    ''' docstring for this function
    generate weekly usage report for the given
    subject (user or remote host)'''
    [put your python code
    for this function here]
    return weekly_usage


def cal_monthly_usage(subject, login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''
    [put your python code
    for this function here]
    return monthly_usage


if __name__ == '__main__':
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)
    '''

    usage_text = '''
        ur_rchan.py [-h] [-l {user,host}] [-r RHOST] [-t {daily,weekly,monthly}]
                     [-u USER] [-v]
                     F [F ...]
        '''

    parser = argparse.ArgumentParser(description="Usage Report based on the last command",
                                     epilog="\nCopyright 2018 - David Nguyen", usage=usage_text)

    parser.add_argument("F", help="list of files to be processed")
    parser.add_argument("-l", "--list", metavar="{user,host}",
                        help="generates user name or remote host IP from the given files")
    parser.add_argument("-r", "--rhost", metavar="RHOST", help="usage report for the given remote host IP")
    parser.add_argument("-t", "--type", metavar="{daily,monthly,weekly}",
                        help="type of report: daily, weekly, and monthly")
    parser.add_argument("-u", "--user", help="usage report for the given user name")
    parser.add_argument("-v", "--verbose", help="tune on output verbosity", action="store_true")

    args = parser.parse_args()