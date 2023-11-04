# Python Address Book Bot

Python Address Book is a simple command-line application that allows you to manage contacts and their phone numbers, along with the option to add birthdays. The application provides functionality to add, change, display, and delete contacts, as well as manage birthdays and view upcoming birthdays for the next week.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [File I/O](#file-io)
- [License](#license)

## Getting Started

To get started with Python Address Book, follow these steps:

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/YevhenNesvit/goitneo-python-hw-3-group-3.git
   ```

2. Navigate to the project directory:
   
   ```
   cd goitneo-python-hw-3-group-3
   ```
3. Run the application:

   ```
   python bot.py
   ```

## Features
- Add Contact: You can add a new contact with a name and phone number.
- Change Contact: Update the phone number for an existing contact.
- Show Phone: Display the phone number for a specific contact.
- All Contacts: View a list of all contacts in the address book.
- Add Birthday: Add a birthday in DD.MM.YYYY format to a contact.
- Show Birthday: Display the birthday for a specific contact.
- Birthdays: View upcoming birthdays for the next week.

## Usage
The application accepts the following commands:

- 'add [name] [phone]': Add a new contact.
- 'change [name] [old_phone] [new_phone]': Update the phone number for an existing contact.
- 'phone [name]': Display the phone number for a specific contact.
- 'all': View all contacts in the address book.
- 'add-birthday [name] [DD.MM.YYYY]': Add a birthday for a specific contact.
- 'show-birthday [name]': Display the birthday for a specific contact.
- 'birthdays': View upcoming birthdays for the next week.
- 'hello': Receive a greeting from the bot.
- 'close or exit': Close the program.

## File I/O

File I/O
The application supports saving and loading the address book to/from a file. You can use the following methods:

- 'save_to_file(filename)': Save the address book to a file.
- 'load_from_file(filename)': Load the address book from a file. If the file doesn't exist, a new empty address book will be created.

To save your address book to a file:

   ```
   address_book.save_to_file('my_address_book.dat')
   ```

To load your address book from a file (during program startup):

   ```
   loaded_address_book = AddressBook.load_from_file('my_address_book.dat')
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit/) for details.
