# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    movies.append({
    'title': input("Enter the movie title: "),
    'director': input("Enter the movie director: "),
    'year': input("Enter the movie release year: ")
    })


def show_movies():
    number = 1
    for movie in movies:
        print(f"{number} Movie")
        print_movie(movie)
        number += 1


def print_movie(movie):
    print(f"Tittle: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    name = input("What movie you looking for")
    for movie in movies:
        if movie['title'] == name:
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()