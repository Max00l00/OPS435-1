#!/usr/bin/env python3

<<<<<<< HEAD
import sys

filelist = sys.argv[1]

=======
import os
>>>>>>> origin/master

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

if __name__ == '__main__':
    print(get_login_rec())

