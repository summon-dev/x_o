from random import randint

# Place the player mark in the position
def update_table(pos, player):
    global ls
    if pos == 0:
        ls = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(3):
        for j in range(3):
            if ls[i][j] == pos:
                ls[i][j] = player
    print_table(ls)     

# Check if the Board is full and Game should be continued
def game_is_on(ls):
    total = 0
    for item in ls:
        total += item.count('X') + item.count('O')
    if total < 9 :
        return True
    if check_winner(ls, 'X') or check_winner(ls, "O"):
        return False

# Check and mark Requsted Player position
def pos_available(pos):
    for item in ls:
        for i in range(3):
            if item[i] == pos:
                return True
    else:
        return False

# Draw the board
def print_table(ls):
    for i in range(3):
        print(f"|{ls[i][0]}|{ls[i][1]}|{ls[i][2]}|")
        if i < 2 : print("+" + "-+" * 3)      
    print("\n")

# Check if a player is a winner
def check_winner(ls, player):
    for item in ls:
        if item.count(player) == 3:
            return True
    
    for i in range(3):
        lh =[]
        for item in ls:
            if item[i] == player:
                lh.append(player)
                if lh.count(player) == 3:
                    return True
    if ls[0][0] == player and ls[1][1] == player and ls[2][2] == player:
        return True
    if ls[0][2] == player and ls[1][1] == player and ls[2][0] == player:
        return True
    return False

# Handle computer game player
def computer_move():
    c_pos = randint(1,9)
    if pos_available(c_pos):
        update_table(c_pos,player="O")
    elif game_is_on(ls):
        computer_move()
            
        
update_table(0,0)

# The Game play 

while game_is_on(ls):
    try:
        pos = int(input("Enter a free position for 'X': "))
    except ValueError:
        print("The position is not a valid position, Please try again:")
    else:
        if pos == 12:
            exit()
        if pos_available(pos):
            update_table(pos, player="X")
            computer_move()
            if check_winner(ls, player="X") and check_winner(ls, "O"):
                print("The Game is tie")
                exit()
            elif check_winner(ls , player="O"):
                print("The Winner is O Player")
                exit()
            if check_winner(ls, player="X"):
                print("The winner is X Player:")          
        else: 
            print("The Position in not available, Please choose another one.")