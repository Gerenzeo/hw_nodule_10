from logic import AddressBook, Record

CONTACTS = AddressBook({'artem': ['0501663395', '05088393122']})


# DECORATOR
def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError as e:
            return f"This user {e} is not exist! Please Add user before using this command!"
        except ValueError:
            return 'Give me name and phone please!'
        except IndexError:
            return 'You enter not corrent name or this name is not exist!'
        except TypeError:
            return 'Please enter name and phone!'
    return inner

def command_hello(*args):
    return 'How can I help you?'

@input_error
def command_add_user(contacts: dict, name, *args):
    if name in contacts:
        return f'Sorry, but contact with name {name.title()} already exist! Please try another name!'
    else:
        record = Record(name)
        
        if args:
            for phone in args:
                record.add_phone(phone)
                
        contacts.add_record(record)
        return f'User {str(record.name).title()} successfully added!'

@input_error
def command_add_phone(contacts: dict, name, phone):
    if name not in contacts:
        return f'Sorry but {name} not found!'
    record = contacts[name]

    if phone in record.phones:
        return f'Sorry, but phone with number {phone} already exist!'

    record.add_phone(phone)
    contacts.add_record(record)
    return f'Phone {phone} successfully added for user {str(name).title()}.'

@input_error
def command_delete_phone(contacts: dict, name, phone):
    if name not in contacts:
        return f'Sorry but {name} not found!'
    record = contacts[name]

    if phone in record.phones:
        record.remove_phone(phone)
        contacts.add_record(record)
        return f'Phone {phone} successfully deleted for user {str(name).title()}.'
    
    return f'User {str(name).title()} don\'t have this number {phone}'

@input_error
def command_change(contacts: dict, name, old_phone, new_phone):
    if name not in contacts:
        raise KeyError(name)
    
    record = contacts[name]
    record.edit_phone(old_phone, new_phone)
    contacts.add_record(record)
    return f'Phone number {old_phone} has been changed to {new_phone} for {str(name).title()}.'

@input_error
def command_phone(contacts: dict, name):
    if name in contacts:
        return contacts[name]
    return f'Sorry, but contact with {name} is not found!'

def command_show_all(contacts: dict):
    for name, numbers in contacts.items():
        print(f'Contact name: {name}')
        print(f'Contact numbers: {numbers}\n')

def command_unknown(command):
    return f'Command [{command}] is not exist!'

COMMANDS = {
    'hello': command_hello,
    'add user': command_add_user,
    'add phone': command_add_phone,
    'delete phone': command_delete_phone,
    'change': command_change,
    'phone': command_phone,
    'show all': command_show_all
}

def main():
   while True:
        command = input('Enter command: ').lower()
        if command in ['exit', 'good bye', 'close']:
            print('Good bye!')
            break
        if command:
            current_command = filter(lambda comanda: command.startswith(comanda), [c for c in COMMANDS.keys()])
            func = ''
            
            try:
                func = command[:len(list(current_command)[0])]
            except IndexError:
                pass
            
            if COMMANDS.get(func):
                handler = COMMANDS.get(func)
                data = command[len(func):].strip()

                if data:  
                    data = data.split(' ')
                result = handler(CONTACTS, *data)
            else:
                result = command_unknown(command)  
            print(result, '\n')
        else:
            print('Please write something!', '\n')


if __name__ == '__main__':
    main()
