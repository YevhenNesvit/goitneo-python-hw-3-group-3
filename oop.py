from collections import UserDict
import re
from datetime import datetime, date
from collections import defaultdict

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
        birthdays_per_week = defaultdict(list)
        today = datetime.today().date()
        users = sorted(book.data.values(), key=lambda x: x.birthday.value)
        
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