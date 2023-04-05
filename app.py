import database


MENU_PROMPT = """-- Fifa Team App --

Please choose one of the options:

1) Add a new team.
2) See all teams.
3) Find a team by name.
4) See which team is the best in fifa.
5) Exit.

Your selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            name = input("Enter team name: ")
            league = input("Enter the name of the league: ")
            rating = int(input("Enter the rating overall (0-100): "))

            database.add_fifa(connection, name, league, rating)
        elif user_input == "2":
            fifa = database.get_all_fifa(connection)
            
            for team in fifa:
                print(f"{team[1]} ({team[2]} - {team[3]}/100)")


        elif user_input == "3":
            name = input("Enter team name to find: ")
            fifa = database.get_fifa_by_name(connection, name)


            for team in fifa:
                print(f"{team[1]} ({team[2]} - {team[3]}/100)")

        elif user_input == "4":
            name = input("Enter team name to find: ")
            best_team = database.get_best_preparation_for_fifa(connection, name)

            print(f"The best team in fifa is {name} which is from the {best_team[2]} ")
        else:
            print("Invalid input, please try again!")
     


menu()
