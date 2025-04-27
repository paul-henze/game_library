class Game: #class game to make the object.
    def __init__(self, name, studio, launch_year, finished=False):
        self.name = name
        self.studio = studio
        self.launch_year = launch_year
        self.finished = finished

    def __str__(self):
        status = "Finished" if self.finished else "Not Finished"
        return f"- {self.name} ({self.launch_year}) - {self.studio} - [{status}]"

#menu and functions
#All games added will go to the library list, I have left some of my favorite games for testing.
library = [
    Game("The Legend of Zelda","Nintendo",1986),
    Game("The Witcher 3","CD PROJEKT RED",2015),
    Game("Cyberpunk 2077","CD PROJEKT RED",2020)
]

def add_game(): #function to add a game to the library
    name = input("Title of the game: ").capitalize()
    studio = input("Studio: ").capitalize()
    while True: #Loop to prevent the user from typing something different of number in the year o release of the game.
        launch_year = input("Which year was this game published: ")
        if launch_year.isdigit() and len(launch_year) == 4:
            break
        else:
            print("Please, the year input should be 4 numbers.")


    game = Game(name, studio, launch_year)
    library.append(game)
    print(f"\n{name} was added to the library!")

def remove_game(): #function to remove a game from the library
    name = input("Type the game title you wish to remove: ")
    for game in library:
        if game.name == name:
            library.remove(game)
            print(f"{name} was removed from the library.")
            return
    print("Error: Game not found.")

def game_list(): #function to show the list of games, in case of no games on the list, a message will appear.
    if library:
        print("\n  Games list:")
        for game in library:
            print(game)
    else:
        print("The library is empty.")

def mark_as_finished(): #function to mark the game title you finished.
    game_list()
    name = input("\nType the game title you wish to mark as finished: ").capitalize()
    for game in library:
        if game.name.lower() == name.lower():
            game.finished = True
            print(f"\n{name} was marked as finished in the library.")
            return
    print("Error: Game not found.")

def menu(): # main menu of the program
    while True:
        try:
            print("-" * 58)
            print("#" * 15, " " * 5, "Games Library", " " * 5, "#" * 15)
            print("-" * 58)
            print("- Select an option:", "\n 1- Add games to the library","\n 2- Remove games from the library","\n 3- View games library","\n 4- Mark a game as finished","\n 5- Exit")
            print("-" * 58)
            option = int(input("Select your option:(1-5) "))
            if option == 1: #calls the function to add a game to the library
                add_game()
            elif option == 2: #calls the function to remove a game from the library
                remove_game()
            elif option == 3: #calls the function to show the list of games
                game_list()
            elif option == 4: #mark the game you finished in the list
                mark_as_finished()
            elif option == 5: #exit the program
                print("Goodbye!")
                break          
            else:
                print("Wrong input, please select one of the options.")
        except ValueError:  #Catch errors
            print("Error: Invalid input. Please, type a number between 1 and 5.")




menu()