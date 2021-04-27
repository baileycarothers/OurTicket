import tables
from dbacc import db_login
from dbacc import db_ticket


logins = db_login("OurTicket")
# logins.add_user("cole_roper", "ThisIsALongPassword559", 0)
tickets = db_ticket("OurTicket")
# tickets.add_ticket(1, 5, "Shaders.", "VISUAL", "We should consider implementing shaders because they are cool.")
# print(tickets.get_ticket(7))
# tickets.upvote_ticket(7)
# print(tickets.get_ticket(7))
# tickets.update_priority()
# print(tickets.get_ticket(7))

del(logins)
del(tickets)


tables.show_table("login")
tables.show_table("ticket")

