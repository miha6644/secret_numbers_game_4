import datetime
import json
import random

# function for booting up the game
def play_game():
    player = input("Hi, what is your name? ")

    secret = random.randint(1, 30)
    attempts = 0

    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())

    for score_dict in score_list:
        score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(
            score_dict.get("player_name"),
            str(score_dict.get("attempts")),
            score_dict.get("date"),
            score_dict.get("secret_number"),
            score_dict.get("wrong_guesses"))
        print(score_text)

    wrong_guesses = []
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player,
                               "secret_number": secret, "wrong_guesses": wrong_guesses})

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

        wrong_guesses.append(guess)

# return a list for all scores
def call_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

# return a list with the top 3 scores
def get_top_scores():
    score_list = call_score_list()
    top_score_list = sorted(score_list, key=lambda s: s["attempts"])[:3]
    return top_score_list

# new game or quit
def new_game_or_quit():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

        if selection.upper() == "A":
            play_game()
        elif selection.upper() == "B":
            for score_dict in get_top_scores():
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        else:
            break
