
import mariadb


class db_table:
    def __init__(self, db):
        # Connect to Database
        try:
            self.connection = mariadb.connect(
                user = "ussr",
                password = "pa55word",
                host = "localhost",
                port = 3306,
                database = db
            )
        except mariadb.Error as e:
            print(f"Error connecting to {db}: {e}")
            sys.exit(1)

        # Get Cursor to Database
        try:
            self.cursor = self.connection.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to {db}: {e}")
            sys.exit(1)

    def disconnect(self):
        self.connection.close()
        del(self)


class db_login(db_table):
    table = "login"

    def get_user(self, uid):
        try:
            self.cursor.execute(f"SELECT * FROM {self.table} WHERE uid={uid};")
            (*user,) = self.cursor
            if len(user) == 0:
                return False
            else:
                return user
        except mariadb.Error as e:
            print(f"Error connecting to {db}: {e}")
            sys.exit(1)

    def add_user(self, name, passh, priv):
        try:
            self.cursor.execute(f"INSERT INTO {self.table} VALUES (0, '{name}', '{passh}', {priv});")
            self.connection.commit()
            return True
        except mariadb.Error as e:
            print(f"Error connecting to {db}: {e}")
            sys.exit(1)


class db_ticket(db_table):
    table = "ticket"

    def get_ticket(self, tid):
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE tid={tid};")
        (*ticket,) = self.cursor
        try:
            if len(ticket) == 0:
                return False
            else:
                return ticket
        except mariadb.Error as e:
            print(f"Error connecting to {db}: {e}")
            sys.exit(1)

    def add_ticket(self, priority, votes, name, category, description):
        try:
            self.cursor.execute(f"INSERT INTO {self.table} VALUES (0, {priority}, {votes}, '{name}', '{category}', '{description}');")
            self.connection.commit()
            return True
        except mariadb.Error as e:
            print(f"Error connecting to {db}: {e}")
            sys.exit(1)

logins = db_login("OurTicket")
logins.add_user("test", "test", 1)
tickets = db_ticket("OurTicket")
tickets.add_ticket(1, 10, "Fix Tickets!", "TICKET", "The ticket system does not work properly and needs to be fixed.")
print(tickets.get_ticket(1))
print("\nSucessfully disconnected.")
