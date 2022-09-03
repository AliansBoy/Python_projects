USER_CHOICE = """
Enter:
- 'a' to add a new movie
- 'l' to list all movie
- 'd' to delete a movie
- 'q' to quit
Your choice: """

user_options = {
    "a": add_movie,
    "l": show_movies,
    "d": delete_movie
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