import random


def write_score(player_name, lives):
    with open("scores.txt", "a") as file:
        file.write(player_name + " " + lives + "\n")


def zad2():
    word_list = []
    used_characters = []
    correct_characters = []
    lives = 100

    player_name = input("Podaj swoje imie")

    with open('Wisielec.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        for item in content.split():
            word_list.append(item.lower())

    game_word = random.choice(word_list)
    print(game_word)

    while True:

        game_state = ''
        for character in game_word:
            if character in correct_characters:
                game_state += character
            else:
                game_state += '_'
        print(game_state)

        if '_' not in game_state:
            print("Koniec gry! Odgadłeś słowo:", game_word)
            break

        print("Wprowadz litere: ", end=" ")
        character = input().lower()

        if character in used_characters:
            print("Litera zostala juz uzyta")
            continue

        used_characters.append(character)

        if character not in game_word:
            lives = lives - 1
            print("Taka litera nie istnieje w słowie")
        else:
            print("Zgadłeś litere")
            correct_characters.append(character)

        print(used_characters)
        print(lives)
    print("Twój wynik:", lives)
    write_score(player_name, str(lives))


zad2()
