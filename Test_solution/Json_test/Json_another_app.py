import json

USER_CHOICE = """
Enter:
- 'a' to add a new birthday
- 'l' to list all birthdays
- 'd' to delete a birthday by date
- 'f' to find by date
- 'q' to quit
Your choice: """


birthday_file = 'birthdays2.txt'


def create_json_file():
    with open(birthday_file, 'w') as file:
        json.dump([], file)


def read_all():
    try:
        with open(birthday_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        create_json_file()
        read_all()


def list_all():
    birthdays = read_all()
    for birthday in birthdays:
        print(f"{birthday['name']} was born {birthday['birthday']}")


def save_all(birthday_list):
    with open(birthday_file, 'w') as file:
        json.dump(birthday_list, file)


def add_item():
    birthdays = read_all()
    name_input = input("Input friend name please: ")
    birthday_input = input("Input friend birthday please: ")
    birthdays.append({'name': name_input, 'birthday': birthday_input})
    save_all(birthdays)


def find_by_date():
    birthdays = read_all()
    birthday_input = input("Input friend birthday please: ")
    try:
        for birth in birthdays:
            if birth['birthday'] == birthday_input:
                print(f"{birth['name']} was born {birth['birthday']}")
    except Exception:
        print("Sorry wrong date")


def delete_by_date():
    birthdays = read_all()
    birthday_input = input("Input friend birthday please: ")
    try:
        birthdays = [birthday for birthday in birthdays if birthday['birthday'] != birthday_input]
        save_all(birthdays)
        list_all()
    except Exception:
        print("Sorry wrong date")

# =============================================================================================================

user_options = {
    'a': add_item,
    'f': find_by_date,
    'l': list_all,
    'd': delete_by_date
}


def menu():
    selection = input(USER_CHOICE)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(USER_CHOICE)


menu()


