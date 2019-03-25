#!/usr/bin/env python3

def read_login_rec(filelist):
    """
    The read_login_rec takes one argument being a given log file name. The function will
    an unformatted list from the data from the the given file.
    """

    x = open(filelist, 'r')
    login_recs = x.readlines()
    x.close()
    filtered_recs = []

    if args.list:                                      # LIST OPTION
        if args.list == 'user':
            for item in login_recs:
                filtered_recs.append(item.split()[0])  # Filter only user names
        if args.list == 'host':
            for item in login_recs:
                filtered_recs.append(item.split()[2])  # Filter only host IPs
        return set(filtered_recs)

    elif args.type:                                    # TYPE OPTION


    else:
        return set(login_recs)


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
        for item in args.filename:
            unformatted_login_recs.extend(read_login_rec(args.filename[0]))

    if args.verbose:
        print('Files to be processed: ' + str(args.filename))
        print('Type of args for files ' + str(type(args.filename)))

        if args.list:
            print('processing usage report for the following:')
            print('reading login/logout record files ' + str(args.filename))
            print('Generating list for ' + str(args.list))
        else:
            if args.rhost:
                print('usage report for remote host: ' + str(args.rhost))
            else:
                print('usage report for user: ' + str(args.user))
            print('usage report type:', str(args.type))
            print('processing usage report for the following:')
            print('reading login/logout record files', str(args.filename))

    if args.type:
        time_frame = {'daily': 'Date', 'weekly': 'Week #', 'monthly': 'Month'}
        print(args.type + ' usage report for ' + args.user or args.rhost)
        print(len(args.type + ' usage report for ' + args.user or args.rhost) * '=')
        if args.type == 'daily':
            print('{:13} {:>13}'.format('Date', 'Usage in seconds'))
        #            print(cal_daily_usage(args.rhost or args.user, unformatted_login_recs))
        elif args.type == 'weekly':
            print('{:12} {:>12}'.format('Week #', 'Usage in seconds'))
        #            print(cal_monthly_usage(args.rhost or args.user, unformatted_login_recs))
        elif args.type == 'monthly':
            print('{:11} {:>11}'.format('Month', 'Usage in seconds'))
        #           print(cal_monthly_usage(args.rhost or args.user, unformatted_login_recs))
