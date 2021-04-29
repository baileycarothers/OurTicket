import sys
import mariadb


class db_table:
    def __init__(self, db):
        # Connect to Database
        try:
            self.connection = mariadb.connect(
                user = "ussr",
                password = "oursecurity",
                host = "localhost",
                port = 3306,
                database = db
            )
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

        # Get Cursor to Database
        try:
            self.cursor = self.connection.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def __del__(self):
        self.disconnect()

    def disconnect(self):
        self.connection.close()
        del(self)


class db_login(db_table):
    table = "login"

    def get_user_by_uid(self, uid):
        try:
            self.cursor.execute(f"SELECT * FROM {self.table} WHERE uid={uid};")
            (*user,) = self.cursor
            if len(user) == 0:
                return False
            else:
                return user[0]
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def get_uid_by_user_pass(self, username, password):
        try:
            self.cursor.execute(f"SELECT uid FROM {self.table} WHERE user=('{username}') AND pass=('{password}');")
            (*uid,) = self.cursor
            if len(uid) == 0:
                return -1
            else:
                return uid[0][0]
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)



    def add_user(self, name, passh, priv):
        try:
            self.cursor.execute(f'''
                INSERT INTO {self.table} (
                    user,
                    pass,
                    priv
                )
                VALUES (
                    '{name}', 
                    '{passh}', 
                    {priv}
                );
            ''')
            self.connection.commit()
            return True
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)


class db_ticket(db_table):
    table = "ticket"

    def get_ticket_by_tid(self, tid):
        print(tid)
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE tid={tid};")
        (*ticket,) = self.cursor
        try:
            if len(ticket) == 0:
                return False
            else:
                return ticket[0]
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def get_tid_by_name(self, name):
        self.cursor.execute(f"SELECT tid FROM {self.table} WHERE (name='{name}');")
        (*ticket,) = self.cursor
        try:
            if len(ticket) == 0:
                return False
            else:
                return ticket[0][0]
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def add_ticket(self, priority, votes, name, category, description):
        try:
            self.cursor.execute(f'''
                INSERT INTO {self.table} (
                    priority,
                    votes,
                    name,
                    category,
                    description
                )
                VALUES (
                    {priority}, 
                    {votes}, 
                    "{name}", 
                    "{category}", 
                    "{description}"
                );'''
            )
            self.connection.commit()
            return True
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def del_ticket(self, tid):
        try:
            self.cursor.execute(f"DELETE FROM {self.table} WHERE tid = {tid};")
            self.connection.commit()
            return True
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def upvote_ticket(self, tid):
        try:
            self.cursor.execute(f"UPDATE OurTicket.{self.table} SET votes = votes + 1 WHERE tid = {tid};")
            self.connection.commit()
            return True
        except mariadb.error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def update_priority(self):
        try:
            self.cursor.execute(f"SELECT tid FROM ticket ORDER BY votes DESC;")
            (*tids,) = self.cursor
            priority = 0
            for tid in tids:
                tid = tid[0]
                self.cursor.execute(f"UPDATE {self.table} SET priority = {priority} WHERE tid = {tid};")
                priority += 1
            self.connection.commit()
        except mariadb.error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)
    
    def get_all_tickets(self):
        self.cursor.execute(f"SELECT * FROM {self.table};")
        (*ticket,) = self.cursor
        try:
            if len(ticket) == 0:
                return False
            else:
                return ticket
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)
    def get_ticket_count(self):
        self.cursor.execute(f"SELECT * FROM {self.table};")
        (*ticket,) = self.cursor
        try:
            return len(ticket)
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)