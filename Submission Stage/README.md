# OurTicket
**Communi**ty-driven is**s**ue tracking syste**m**

# CHANGELOG:
4/28/2021:
	Rebuilt database from scratch
	Added command line interface for db access
	Added php files suitable for webserver use with behavior to allow the opening, closing, and voting on of tickets in the web browser
	Extended python scripts to provide enhanced functionality for developers

## Main Features

1. Online Database-Centric Backend
2. Open / Close / Read Ticket
3. Categorizable Ticket Class
4. Ticket Priority
5. User Privilege Levels

## Installation
Setup assumes a functioning PHP installation, python 3+, and a mariaDB database.
Database must be configured by the user in dbaccess, tables, and ticket_access.

1. Place Source in desired directory.
2. Symlink Web to /var/www/html/Source or /var/www/Source, depending on your webserver and Linux configuration.


## Usage
Ensure the webserver is active, and visit 
	1. https://hostname/Web/submit_new.php to create new tickets
	2. https://hostname/Web/read_posts.php to read all current tickets, or close or vote on them.

## Support
For support check the [Github](https://github.com/baileycarothers/OurTicket)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
