import random

card_array = []
player_name_array = []

suitName = ("Hearts", "Diamonds", "Spades", "Clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")

print("\n", suitName, "\n")
print("\n", rankName, "\n")
print("please select one of rank and suit above:\n")

global total_player


def game_task():
    player_count = 0
    while player_count < total_player:
        input_title_player_nm = "Please enter " + str(
            player_count+1)+" player Name \n"
        player_name = input(input_title_player_nm)
        if player_name == "--help":
            print("print help data here")
        elif player_name == "--resume":
            print("Resume here")
        elif player_name != "--help" and player_name != "--resume":
            player_count += 1
            player_name_array.append(player_name)
            if player_count == total_player:
                card_count = 0
                while card_count < total_player:
                    input_title_pick_card = "Please " + str(
                        player_name_array[card_count])+" pick the card : \n"
                    set_card = input(input_title_pick_card)
                    if set_card == "--help":
                        print("print help data here")
                    elif set_card == "--resume":
                        print("Resume here")
                    elif set_card != "--help" and set_card != "--resume":
                        card_count += 1
                        card_array.append(set_card)


global total_player_str
while True:
    try:
        total_player_str = input(
            "How many players are going to play the game? please enter : ")
        total_player = int(total_player_str)
        game_task()

        for total_player_loop in range(total_player):

            print(player_name_array[total_player_loop], "has",
                  card_array[total_player_loop], "card")

        break

    except ValueError:

        if total_player_str == "--help":
            print("Help \n"
                  "1.Enter players from One \n"
                  "2.Can take Help by typing --help \n"
                  "3.First enter only Names of Players \n"
                  "4.Enter cards \n"
                  "5.Can resume your status by typing __resume \n")
        elif total_player_str == "--resume":
            print("Resume here")
        else:
            print("This is not a number")
