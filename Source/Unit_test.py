#!/usr/bin/python3
#Unit Test 1

import unittest
from dbacc import db_ticket

class TestAccessMethods(unittest.TestCase):
    def test_create_and_find(self):
        ticket = db_ticket("OurTicket")
        ticket.add_ticket(0, 0, "1", "2", "3")
        result = ticket.get_ticket_by_tid(ticket.get_tid_by_name("1"))
        print(result)
        
if __name__ == '__main__':
    unittest.main()
        