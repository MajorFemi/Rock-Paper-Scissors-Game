import random
print("*** Rock-Paper-Scissors Game ***")
Player = input("Enter your preferred player name: ")
print(f"Welcome {Player}!\n Note that: R - Rock, P - Paper, S - Scissors \n Let's Go!")
list_of_outcomes = ["R", "P", "S"]

def get_player_move():
    while True:
        Player_move = (input("Enter your move (R, P or S): ").upper())
        if Player_move not in ("R", "P", "S"):
            print("Not among the option, Kindly choose a move in the option")
            continue
        else:
             break
    return Player_move

def get_computer_move():
    CPU = random.choice(list_of_outcomes)
    return CPU

def draw(Player_move, CPU):
    if Player_move == CPU:
        return True

def get_winner(Player_move, CPU):
    if (Player_move == "R") & (CPU == "S"):
        print(f'Rock dismantles Scissors! {Player} is the winner.')
    elif (Player_move == "P") & (CPU == "R"):
        print(f'Paper covers Rock!, {Player} is the winner')
    elif (Player_move == "S") & (CPU == "P"):
        print(f'Scissors slices Paper!, {Player} is the winner.')
    else:
        print('CPU is the winner.')


while True:
    Player_move = get_player_move()
    CPU = get_computer_move()
    print(f'{Player} {Player_move} :  CPU {CPU}')
    if draw(Player_move, CPU):
        print(f"It is a tie! Let's play again, {Player}")
        continue
    else:
        get_winner(Player_move, CPU)
        break
