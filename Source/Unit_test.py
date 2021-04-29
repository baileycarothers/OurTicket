#!/usr/bin/python3
#Unit Test 1

import unittest
from dbacc import db_ticket

class TestAccessMethods(unittest.TestCase):
    
    # Successful Test #1
    def test_create_and_find(self):
        ticket = db_ticket("OurTicket")
        ticket.add_ticket(0, 0, "1", "2", "3")
        tid = ticket.get_tid_by_name("1")
        result = ticket.get_ticket_by_tid(tid)
        self.assertEqual(result, (tid, 0, 0, '1', '2', '3'))
    
    
    def test_upvote(self):
        ticket = db_ticket("OurTicket")
        tid = ticket.get_tid_by_name("1")
        ticket.upvote_ticket(tid)
        result = ticket.get_ticket_by_tid(tid)
        self.assertEqual(result, (tid, 0, 1, '1', '2', '3'))
    
    # Successful Test #3
    def test_remove(self):
        ticket = db_ticket("OurTicket")
        
        tid = ticket.get_tid_by_name("1")
        ticket.del_ticket(tid)
        result = ticket.get_ticket_by_tid(tid)
        self.assertEqual(result, False)
        
    
    
if __name__ == '__main__':
    unittest.main()
        