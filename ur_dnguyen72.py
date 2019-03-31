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
    for record in results:
        if len(record.split()) == 15:
            login_recs.append(record)
    return login_recs


def read_login_rec(filelist):
    """
    The read_login_rec takes one argument being a given log file name. The function will take the contents of the given
    file and return the contents of the file in a set removing all duplicate contents.

    If the argument list is given when running the script, the read_login_rec function will filter out either only users
    or hosts depending on what option was given to the list argument.

    Example:

        print(read_login_rec(text.txt))

       ['This is the contents of the text file']
    """

    x = open(filelist, 'r')
    login_recs = x.readlines()
    x.close()
    filtered_recs = []

    if args.list:
        if args.list == 'user':
            for record in login_recs:
                filtered_recs.append(record.split()[0])  # Grab only user names
        if args.list == 'host':
            for record in login_recs:
                filtered_recs.append(record.split()[2])  # Grab only host IPs
        return filtered_recs
    else:
        return login_recs


def convert_days(login_recs):
    """
    The convert_days function takes one argument being a login record from the read_login_rec function. It
    will take this record and convert all log records where the login date differs from the logout date to
    multiple log records where the login and logout dates are the same. The function will return a new
    converted login record with the new login/logout conversions.

    Example:

        login_recs

        user5   pts/0    192.0.172.162    Mon Dec 25 23:36:57 2017 - Tue Dec 26 00:25:37 2017  (00:48)

        convert_days(login_recs)

        user5   pts/0    192.0.172.162    Mon Dec 25 23:36:57 2017 - Mon Dec 26 23:59:59 2017  (00:48)
        user5   pts/0    192.0.172.162    Tue Dec 25 00:00:00 2017 - Tue Dec 26 00:25:37 2017  (00:48)
    """

    converted_record = []
    for record in login_recs:
        #   Login/out Structured Time
        login_rec = time.strptime(' '.join(record.split()[3:8]), "%a %b %d %H:%M:%S %Y")
        logout_rec = time.strptime(' '.join(record.split()[9:14]), "%a %b %d %H:%M:%S %Y")
        #   Login/out doy (Day of Year)
        login_doy = time.strftime("%j", login_rec)
        logout_doy = time.strftime("%j", logout_rec)

        #   If login/out is in same day
        if login_doy == logout_doy:
            converted_record.append(record.split())

        #   If login/out are on different days
        else:
            # SEPARATE LOGIN DAY
            login_rec_float = time.mktime(login_rec)  # float number
            eod_data = time.ctime(login_rec_float).split()  # End of day data
            new_login_day = record.split()
            new_login_day[9:12] = eod_data[0:3]
            new_login_day[12] = '23:59:59'
            new_login_day[13] = eod_data[4]
            converted_record.append(new_login_day)

            # SEPARATE LOGOUT DAY(S)
            while login_doy != logout_doy:
                next_day = login_rec_float + 86400  # Add day
                new_day_data = time.ctime(next_day).split()  # Start of Day
                new_logout_day = record.split()
                new_logout_day[3:6] = new_day_data[0:3]
                new_logout_day[6] = '00:00:00'
                new_logout_day[7] = new_day_data[4]
                login_doy = time.strftime('%j', time.localtime(next_day))

                #   If Next Day != Logout Day after adding day
                if login_doy != logout_doy:
                    new_logout_day[9:12] = new_day_data[0:3]
                    new_logout_day[12] = '23:59:59'
                    new_logout_day[13] = new_day_data[4]
                converted_record.append(new_logout_day)
    return converted_record


def cal_usage(subject, converted_record):
    total_usage = 0
    date_usage = {}

    for record in converted_record:
        if subject in record:
            time_pool = time.mktime(time.strptime(' '.join(record[9:14])))
            time_used = time.mktime(time.strptime(' '.join(record[3:8])))
            usage = int(time_pool - time_used)
            time_frame_format = {'daily': '%Y %m %d', 'weekly': '%Y %W', 'monthly': '%Y %m'}
            time_format = time.strftime(time_frame_format[args.type], time.strptime(' '.join(record[9:14])))

            try:
                date_usage[time_format] += usage
            except:
                date_usage[time_format] = usage
            total_usage += usage
    output = []
    for key in sorted(date_usage.keys(), reverse=True):
        output.append("{:<11s}{:>11d}".format(str(key), date_usage[key]))
    output.append("{:<11s}{:>11d}".format("Total", total_usage))
    return output


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
        for record in args.filename:
            unformatted_login_recs.extend(read_login_rec(record))

    if args.verbose:
        print('Files to be processed: ' + str(args.filename))
        print('Type of args for files ' + str(type(args.filename)))

        if args.list:
            print('processing usage report for the following:')
            print('reading login/logout record files ' + str(args.filename))
            print('Generating list for ' + str(args.list))
        else:
            if args.rhost:
                print('Usage Report for remote host: ' + str(args.rhost))
            else:
                print('Usage Report for user: ' + str(args.user))
            print('usage report type:', str(args.type))
            print('processing usage report for the following:')
            print('reading login/logout record files', str(args.filename))

    if args.list:
        print(args.list.title() + ' list for ' + ' '.join(args.filename))
        print(len(str(args.list) + ' list for ' + ''.join(args.filename)) * '=')
        print(*sorted(unformatted_login_recs), sep="\n")

    if args.type:
        print(args.type.title() + ' usage report for ' + str(args.user or args.rhost))
        print(len(args.type.title() + ' Usage Report for ' + str(args.user or args.rhost)) * '=')
        time_frame = {'daily': 'Date', 'weekly': 'Week #', 'monthly': 'Month'}
        print("{:<14s}{:>14s}".format(time_frame[args.type], "Usage in Seconds"))
        print(*cal_usage(args.rhost or args.user, convert_days(unformatted_login_recs)), sep='\n')