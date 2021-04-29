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
        print(result)
        self.assertEqual(result, (tid, 0, 0, '1', '2', '3'))
    
    def test_remove(self):
        
        tid = ticket.get_tid_by_name("1")
        result = get_ticket_by_tid(tid)
        self.assertEqual(result, false)
    
if __name__ == '__main__':
    unittest.main()
        