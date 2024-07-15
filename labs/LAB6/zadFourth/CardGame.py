import random

from labs.LAB6.zadFourth.Card import Card

player_one_points = 0
player_two_points = 0

card_list = {"Two": 2,
             "Three": 3,
             "Four": 4,
             "Five": 5,
             "Six": 6,
             "Seven": 7,
             "Eight": 8,
             "Nine": 9,
             "Ten": 10,
             "Jack": 11,
             "Queen": 12,
             "King": 13,
             "Ace": 14}

colors = ['Karo', 'Kier', 'Trefl', 'Pik']

talia = [Card(value, color, card_list[value]) for color in colors for value in card_list]

while True:

    input("Naciśnij dowolony przycisk")

    player_one_card = random.choice(talia)
    player_two_card = random.choice(talia)

    if player_one_card.get_points() > player_two_card.get_points():
        print(str(player_one_card) + " vs " + str(player_two_card))
        print("PlayerOne lepszy")
        player_one_points += 1
    elif player_one_card.get_points() < player_two_card.get_points():
        print(str(player_one_card) + " vs " + str(player_two_card))

        print("PlayerTwo lepszy")
        player_two_points += 1
    else:
        print("Remis")

    print("Punkty gracza jeden: " + str(player_one_points))
    print("Punkty gracza dwa: " + str(player_two_points))
