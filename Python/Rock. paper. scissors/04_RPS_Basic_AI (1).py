#!/usr/bin/python3

import random
from enum import IntEnum


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}


def assess_game(user_action, computer_action):
    game_result = None
    
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    return game_result

            
def get_computer_action(user_actions_history, game_history):
    # No previous user actions => random computer choice
    if not user_actions_history or not game_history:
        computer_action = get_random_computer_action()
    # Basic AI functionality
    # 1) If the user won the last round, he may repeat the last choice
    # 2) If the user lost the last round, he may change to the next action in the sequence
    # 3) If user and computer tied in the last round, then get a random computer choice
    else:
        # Path 1)
        if game_history[-1] == GameResult.Victory:
            computer_action = get_winner_action(user_actions_history[-1])
        # Path 2)
        elif game_history[-1] == GameResult.Defeat:
            computer_action = GameAction((user_actions_history[-1].value + 2) % len(GameAction))
        # Random choice
        else:
            computer_action = get_random_computer_action()

    print(f"Computer picked {computer_action.name}.")
    
    return computer_action
            

def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)
       
    return user_action


def get_random_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)

    return computer_action


def get_winner_action(game_action):
    return Victories[game_action]


def play_another_round():
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'n'
        

def main():
    game_history = []
    user_actions_history = []
    
    while True:
        try:
            user_action = get_user_action()
        except ValueError as e:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user_actions_history, game_history)
        user_actions_history.append(user_action)
        game_result = assess_game(user_action, computer_action)
        game_history.append(game_result)
        if not play_another_round():
            break
        

if __name__ == "__main__":
    main()
