import mariadb
import sys


CONN = mariadb.connect(
            user = "ussr",
            password = "oursecurity",
            host = "localhost",
            port = 3306,
            database = "OurTicket"
        )
CURS = CONN.cursor()

def create_tables():
    # login table
    CURS.execute('''
        CREATE TABLE login(
            uid     INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            user    VARCHAR(16) CHARACTER SET utf8,
            pass    VARCHAR(64) CHARACTER SET utf8,
            priv    TINYINT UNSIGNED
        );
    ''')
    # ticket table
    CURS.execute('''
        CREATE TABLE ticket(
            tid         INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            priority    INT,
            votes       INT,
            name        VARCHAR(16)  CHARACTER SET utf8,
            category    VARCHAR(64)  CHARACTER SET utf8,
            description VARCHAR(512) CHARACTER SET utf8
        );
    ''')


def drop_table(table):
    CURS.execute(f"DROP TABLE {table};")


def show_table(table):
    print(f"\n{table}\n================================================================================")
    CURS.execute(f"SHOW COLUMNS FROM {table};")
    for row in CURS:
        print(row)
    print()
    CURS.execute(f"SELECT * FROM {table};")
    for row in CURS:
        print(row)
    print()


# create_tables()
# show_table("login")
# show_table("ticket")
# drop_table("login")
# drop_table("ticket")

