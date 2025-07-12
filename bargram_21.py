import random

def show_rules():
    print("\nWelcome to the 21 Number Game!")
    print("Rules:")
    print("1. Players take turns to count up from 1 to 21.")
    print("2. On your turn, you can say 1, 2 or 3 consecutive numbers.")
    print("3. Whoever says '21' loses.")
    print("4. You can choose to go first or second.\n")

def is_consecutive(player_numbers):
    return all(player_numbers[i] == player_numbers[i - 1] + 1 for i in range(1, len(player_numbers)))

def player_turn(current):
    print(f"\nCurrent number: {current}")
    while True:
        try:
            nums = input("Your turn (Enter 1-3 consecutive numbers separated by space): ").strip().split()
            player_numbers = list(map(int, nums))
            if len(player_numbers) < 1 or len(player_numbers) > 3:
                raise ValueError
            if player_numbers[0] != current + 1:
                raise ValueError
            if not is_consecutive(player_numbers):
                raise ValueError
            return player_numbers
        except:
            print("Invalid input. Make sure you enter 1-3 **consecutive** numbers starting from the next number.")

def computer_turn(current):
    count = (4 - (current % 4)) if (current % 4 != 0) else random.randint(1, 3)
    comp_numbers = [current + i for i in range(1, count + 1)]
    print(f"\nComputer plays: {' '.join(map(str, comp_numbers))}")
    return comp_numbers

def play_game():
    show_rules()
    turn = input("Do you want to go first? (y/n): ").strip().lower()
    current = 0
    player_first = turn == 'y'

    while current < 21:
        if player_first:
            player_nums = player_turn(current)
            current = player_nums[-1]
            if current >= 21:
                print("\nYou said 21. You lose!")
                return
            comp_nums = computer_turn(current)
            current = comp_nums[-1]
            if current >= 21:
                print("\nComputer said 21. You win!")
                return
        else:
            comp_nums = computer_turn(current)
            current = comp_nums[-1]
            if current >= 21:
                print("\nComputer said 21. You win!")
                return
            player_nums = player_turn(current)
            current = player_nums[-1]
            if current >= 21:
                print("\nYou said 21. You lose!")
                return

# Start the game
play_game()
