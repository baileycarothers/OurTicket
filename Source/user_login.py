#!/usr/bin/python3

import sys, getopt
from dbacc import db_login


def main(argv):
    f_register = False
    try:
        opts, args = getopt.getopt(argv, "ru:p:",["username=","password="])
    except getopt.GetoptError:
        print("user_login.py -u <username> -p <password>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-r", "--register"):
            f_register = True
        else:
            print("user_login.py -u <username> -p <password>")
            sys.exit(2)
    login = db_login("OurTicket")
    uid = login.get_uid_by_user_pass(username, password)
    if uid == -1 and not f_register:        # need to register
        print("Incorrect username and password. Please register.")
        sys.exit(2)
    elif uid == -1 and f_register:          # register
        login.add_user(username, password, 2)
        print("Thank you for registering! Please log in.")
        sys.exit(0)
    elif not uid == -1 and not f_register:  # login
        user = login.get_user_by_uid(uid)
    else:
        print("Error encountered.")
        sys.exit(-1)

    #          uid,   uname,    priv
    return user[0], user[1], user[3]


if __name__ == "__main__":
    main(sys.argv[1:])
