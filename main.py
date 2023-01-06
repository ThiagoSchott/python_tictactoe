import os

def draw(positions):  # Draws the game
    board = (
        f"|{positions[1]}|{positions[2]}|{positions[3]}|\n"
        f"|{positions[4]}|{positions[5]}|{positions[6]}|\n"
        f"|{positions[7]}|{positions[8]}|{positions[9]}|\n"
    )
    print("######################")
    print("  SUPER TIC TAC TOE!")
    print("######################\n")
    print(board)

def check_turn(turn):  # Checks who's turn it is
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

def check_choice(choice, positions):  # Checks if input is valid
    if str.isdigit(choice):
        if int(choice) >= 0 and int(choice) < 10: 
            if positions[int(choice)] not in "XO":
                return True
            else: 
                return False
    else:
        return False
        
def check_win(positions):
    # Checks for horizontal wins
    if (positions[1] == positions[2] == positions[3]) \
        or (positions[4] == positions[5] == positions[6]) \
        or (positions[7] == positions[8] == positions[9]):  
        return True
    # Checks for vertical wins
    elif (positions[1] == positions[4] == positions[7]) \
        or (positions[2] == positions[5] == positions[8]) \
        or (positions[3] == positions[6] == positions[9]):  
        return True
    # Cheks for diagonal wins
    elif (positions[1] == positions[5] == positions[9]) \
        or (positions[7] == positions[5] == positions[3]):  
        return True
    else:
        return False

def play(): 
    positions = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
    loop = True
    has_winner = False
    turn = 0
    previous_turn = -1
    while loop:
        os.system('cls' if os.name == 'nt' else 'clear')  # This keeps the terminal clear on each refresh
        draw(positions)
        if previous_turn == turn:
            print("Your input was not valid, please insert again!\n")
        previous_turn = turn
        choice = input("Player " + str(((turn) % 2) + 1) + ", which position do you choose? (Press '0' to quit)\n")
        if int(choice) == 0:
            loop = False
        else:
            is_valid = check_choice(choice, positions)  # Checks if input is valid
            if is_valid:
                turn += 1
                positions[int(choice)] = check_turn(turn)
                if check_win(positions):
                    loop = False
                    has_winner = True
                if turn > 8:
                    loop = False  
    os.system('cls' if os.name == 'nt' else 'clear')  # This keeps the terminal clear on each refresh
    draw(positions)
    if has_winner:  # Checks if game ended
        if check_turn(turn) == "X":
            print("Congrats Player 1, you WON!!\n")   
        else:
            print("Congrats Player 2, you WON!!\n")   
    else:
        print("The game TIED!! Congrats to both players!\n")
        
play()