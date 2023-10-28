import oop

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            if func.__name__ == 'show_phone' and len(args[0]) != 1 :
                return "Enter user name"
            elif func.__name__ == 'add_contact' and args[0][0] in args[1] :
                    return f"Contact {args[0][0]} already exist. To update contact enter 'change name phone'!"
            elif func.__name__ == 'change_contact' and args[0][0] not in args[1] :
                return f"Contact {args[0][0]} does not exist. To add contact enter 'add name phone'!"
            elif not args[0] :
                return "There are no contacts yet!"
            else:
                return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact does not exist. Please try again!"
        except IndexError:
            return "Invalid command format! Command must be followed by name and phone"
    return wrapper

@input_error
def add_contact(args, book):
    name, phone = args
    contact = oop.Record(name)
    contact.add_phone(phone)
    book.add_record(contact)

    return "Contact added."
    
@input_error   
def change_contact(args, book):
    name, phone = args
    contact = book.find(name)
    if contact:
        contact.add_phone(phone)

    return "Contact updated."

@input_error
def show_phone(args, book) :
    name = args[0]
    contact = book.find(name)
    if contact:
        return contact.phones[0]

@input_error    
def show_all(book) :
    all_contacts = [str(contact) for contact in book.data.values()]
    if all_contacts:
        return "\n".join(all_contacts)
    
@input_error    
def add_birthday(args, book) :
    name, birthday = args
    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
        return "Birthday added."

def main():
    book = oop.AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()