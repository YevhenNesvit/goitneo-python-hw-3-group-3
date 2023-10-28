from oop import AddressBook, Record

def parse_input(user_input):
    """
    Parse user input and extract the command and arguments.

    Args:
        user_input (str): User's input string.

    Returns:
        Tuple: A tuple containing the command and arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    """
    Decorator function to handle input validation and errors for command functions.

    Args:
        func (function): The command function to be decorated.

    Returns:
        function: The decorated function with error handling.
    """
    def wrapper(*args, **kwargs):
        try:
            if func.__name__ == 'show_phone' and len(args[0]) != 1 :
                return "Enter user name"
            elif func.__name__ == 'add_contact' and args[0][0] in args[1] :
                    return f"Contact {args[0][0]} already exist. To update contact enter 'change name phone'!"
            elif func.__name__ in ('change_contact', 'show_birthday') and args[0][0] not in args[1] :
                return f"Contact {args[0][0]} does not exist. To add contact enter 'add name phone'!"
            elif not args[0] :
                return "There are no contacts yet!"
            elif func.__name__ == 'add_birthday' and len(args[0]) != 2 :
                return "Give me name and birthday please."
            elif func.__name__ == 'show_birthday' and not args[1][args[0][0]].birthday :
                return "Contact has no birthday yet. To add birthday enter 'add-birthday name birthday'!"
            elif func.__name__ == 'change_contact' and len(args[0]) != 3 :
                return "Give me name, old phone and new phone please."
            else:
                return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact does not exist. Please try again!"
        except IndexError:
            return "Invalid command format! Command must be followed by the parameters"
    return wrapper

@input_error
def add_contact(args, book):
    """
    Add a new contact to the address book.

    Args:
        args (list): A list of arguments containing the name and phone number.
        book (AddressBook): The address book instance to add the contact to.

    Returns:
        str: A message indicating the result of the operation.
    """
    name, phone = args
    contact = Record(name)
    no_error = contact.add_phone(phone)

    if no_error:  
        book.add_record(contact)
        return "Contact added."
    
    return "Contact is not added"
    
@input_error   
def change_contact(args, book):
    """
    Change the phone number for an existing contact in the address book.

    Args:
        args (list): A list of arguments containing the name, old phone, and new phone.
        book (AddressBook): The address book instance to modify the contact.

    Returns:
        str: A message indicating the result of the operation.
    """
    name, old_phone, new_phone = args
    contact = book.find(name)
    if contact:
        contact.edit_phone(old_phone, new_phone)

    return "Contact updated."

@input_error
def show_phone(args, book) :
    """
    Display the phone number for an existing contact in the address book.

    Args:
        args (list): A list of arguments containing the name of the contact.
        book (AddressBook): The address book instance to retrieve the phone number from.

    Returns:
        str: The phone number of the contact or an error message.
    """
    name = args[0]
    contact = book.find(name)
    if contact:
        return contact.phones[0]

@input_error    
def show_all(book) :
    """
    Display all contacts in the address book.

    Args:
        book (AddressBook): The address book instance to retrieve contacts from.

    Returns:
        str: A string containing all contacts or an error message if no contacts exist.
    """
    all_contacts = [str(contact) for contact in book.data.values()]
    if all_contacts:
        return "\n".join(all_contacts)
    
@input_error    
def add_birthday(args, book) :
    """
    Add a birthday to an existing contact in the address book.

    Args:
        args (list): A list of arguments containing the name and birthday.
        book (AddressBook): The address book instance to modify the contact.

    Returns:
        str: A message indicating the result of the operation.
    """
    name, birthday = args
    contact = book.find(name)
    no_error = contact.add_birthday(birthday)
    
    if contact and no_error:
        contact.add_birthday(birthday)
        return "Birthday added."
    
    return "Birthday is not added"

@input_error
def show_birthday(args, book) :
    """
    Display the birthday for an existing contact in the address book.

    Args:
        args (list): A list of arguments containing the name of the contact.
        book (AddressBook): The address book instance to retrieve the birthday from.

    Returns:
        str: The birthday of the contact or an error message.
    """
    name = args[0]
    contact = book.find(name)
    if contact and contact.birthday:
        return contact.birthday

@input_error    
def birthdays(book) :
    """
    Get upcoming birthdays for the week and format them.

    Args:
        book (AddressBook): The address book instance to retrieve contact birthdays.

    Returns:
        str: A string containing upcoming birthdays formatted by weekday.
    """
    return book.get_birthdays_per_week()

def main():
    """
    Main function to run the assistant bot program.
    """
    book = AddressBook.load_from_file('my_address_book.dat')
    print("Welcome to the assistant bot!")
    if book:
        print("Loaded contacts:")
        for contact in book.data.values():
            print(contact)
    else:
        print("No saved address book found. Starting with an empty address book.")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            book.save_to_file('my_address_book.dat')
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()