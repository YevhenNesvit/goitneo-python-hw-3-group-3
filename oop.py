from collections import UserDict
from datetime import datetime, date
from collections import defaultdict
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("The phone number must contain 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            date_obj = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(date_obj.strftime('%d.%m.%Y'))
        except ValueError:
            raise ValueError("Date of birth should be in DD.MM.YYYY format.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ''

    def add_phone(self, phone):
        try:
            new_phone = Phone(phone)
            self.phones.append(new_phone)
            return True
        except ValueError as e:
            print(e)
            return False
        
    def add_birthday(self, birthday):
        try:
            self.birthday = Birthday(birthday)
            return True
        except ValueError as e:
            print(e)
            return False

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        if not self.remove_phone(old_phone):
            return False
        return self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(book) :
        """
        Calculate and return a string representation of birthdays for the upcoming week.

        Args:
            book (AddressBook): An AddressBook instance containing contact information.

        Returns:
            str: A string representing birthdays sorted by weekday.
        """
        birthdays_per_week = defaultdict(list)
        today = datetime.today().date()
        users = book.data.values()
        
        for user in users :
            name = user.name.value
            birthday = user.birthday.value if user.birthday else None
            if birthday:
                birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
        
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year < today :
                birthday_this_year = birthday.replace(year=today.year + 1)
        
            delta_days = (birthday_this_year - today).days
            if delta_days < 7 :
                if birthday_this_year.strftime('%A') in ('Saturday', 'Sunday') :
                    if delta_days > 5 :
                        continue
                    else :
                        birthdays_per_week['Monday'].append(name)
                else :
                    birthdays_per_week[birthday_this_year.strftime('%A')].append(name)
        
        this_week = ""
        for k, v in sorted(birthdays_per_week.items()):
            if v:
                if len(v) > 1:
                    this_week += f"{k} : {', '.join(v)}\n"
                else:
                    this_week += f"{k} : {v[0]}\n"

        return this_week
    
    def save_to_file(self, filename):
        """
        Save the address book to a file.

        This method serializes the address book data and stores it in the specified file.

        Args:
            filename (str): The name of the file to which the address book data will be saved.

        Returns:
            None
        """
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    @classmethod
    def load_from_file(cls, filename):
        """
        Load the address book from a file.

        This method deserializes address book data from the specified file and returns a new
        AddressBook object containing the loaded data. If the file doesn't exist or is empty,
        it returns a new empty AddressBook.

        Args:
            filename (str): The name of the file from which to load the address book data.

        Returns:
            AddressBook: An AddressBook object containing the loaded address book data.
        """
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                address_book = cls()
                address_book.data = data
                return address_book
        except FileNotFoundError:
            return cls()
