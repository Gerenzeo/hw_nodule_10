from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
        
class Name(Field):
    pass
    
class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        for el in self.phones:
            if el == phone:
                return f'Phone with number {phone} already exist!'
        
        self.phones.append(str(Phone(phone)))
        return f'Phone {phone} successfuly added!'
    
    def remove_phone(self, phone):
        if phone in self.phones:
            for index, el in enumerate(self.phones):
                if el == phone:
                    del self.phones[index]
                    return f'Phone {phone} was deleted!'

        return f'Sorry this number is not exist!' 

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            for index, number in enumerate(self.phones):
                if old_phone == number:
                    self.phones[index] = Phone(new_phone)
                    return f'Phone with number {old_phone} successfully change at {new_phone}'
            
        return f'Number with {old_phone} not found!'

    def __str__(self):
        return f'{self.phones}'

    def __repr__(self):
        return f'{self.phones}'
