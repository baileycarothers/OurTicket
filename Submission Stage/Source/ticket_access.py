#!/usr/bin/python3

import sys, getopt
from dbacc import db_ticket


def main(argv):
    f_add = False
    f_find = False
    f_tid = -1
    f_remove = False
    f_vote = False
    f_count = False
    f_all = False
    ticket_name = ""
    ticket_category = ""
    ticket_description = ""
    priv = -1
    try:
        opts, args = getopt.getopt(argv, "gazfrvn:c:d:p:i:",["ticket_name=","ticket_category=","ticket_description="])
    except getopt.GetoptError:
        print(argv)
        print("ticket_access top [SWITCH] [OPTION]")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-a", "--add"):
            f_add = True
        elif opt in ("-f", "--find"):
            f_find = True
        elif opt in ("-i", "--tid"):
            f_tid = arg
        elif opt in ("-z", "--znum_all"):
            f_all = True
        elif opt in ("-r", "--remove"):
            f_remove = True
        elif opt in ("-g", "--get-count"):
            f_count = True
        elif opt in ("-v", "--vote"):
            f_vote = True
        elif opt in ("-n", "--name"):
            ticket_name = arg
        elif opt in ("-c", "--category"):
            ticket_category = arg
        elif opt in ("-d", "--description"):
            ticket_description = arg
        elif opt in ("-p", "--priv"):
            priv = int(arg)
        else:
            print(opts)
            print("ticket_access [SWITCH] [OPTION]")
            sys.exit(2)

    # Parse switches
    if not f_add+f_find+f_remove+f_all+f_count== 1:
        print("Incorrect amount of switches.")
        print("ticket_access [SWITCH] [OPTION]")
        sys.exit(2)

    ticket = db_ticket("OurTicket")
    if f_add:
        if ticket_name == "" or ticket_category == "" or ticket_description == "":
            print("Ticket must have a name, category, and description.")
            sys.exit(2)
        else:
            print(ticket_name, ticket_category, ticket_description)
            ticket.add_ticket(0, 1, ticket_name, ticket_category, ticket_description)
            ticket.update_priority()
            print("Ticket added successfully!")
            sys.exit(0)
    elif f_find:    # no implementation
       # tick = ticket.get_ticket_by_tid(f_tid)
        #for row in tick:
         #   print(row)
        #print(f_vote)
        if(f_tid == -1): return
        if(f_vote):
            ticket.upvote_ticket(f_tid)
    elif f_all:
        tick = ticket.get_all_tickets()
        for t in tick:
            for row in t:
                print(row)
    elif f_count:
        print(ticket.get_ticket_count())
    elif f_remove:
        if priv == 0:
            #tid = ticket.get_tid_by_name(ticket_name)
            print(f_tid)
            ticket.del_ticket(f_tid)
            print(f"{ticket_name} removed successfully.")
            sys.exit(0)
        else:
            print("You do not have the privileges to close tickets.")
            sys.exit(2)
    else:
        print("Incorrect bottom amount of switches.")
        print("ticket_access [SWITCH] [OPTION]")
        sys.exit(2)




if __name__ == "__main__":
    main(sys.argv[1:])
