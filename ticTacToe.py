#Dyllan Spooner          11/03/25

#Making a tictactoe game through lists in python

import random


def drawCondition(gameboard):
    drawCheck = False
    if gameboard[0][0] == 'x' or gameboard[0][0] == 'o':
        if gameboard[0][1] == 'x' or gameboard[0][1] == 'o':
            if gameboard[0][2] == 'x' or gameboard[0][2] == 'o':
                if gameboard[1][0] == 'x' or gameboard[1][0] == 'o':
                    if gameboard[1][1] == 'x' or gameboard[1][1] == 'o':
                        if gameboard[1][2] == 'x' or gameboard[1][2] == 'o':
                            if gameboard[2][0] == 'x' or gameboard[2][0] == 'o':
                                if gameboard[2][1] == 'x' or gameboard[2][1] == 'o':
                                    if gameboard[2][2] == 'x' or gameboard[2][2] == 'o':
                                        drawCheck = True


    
    return drawCheck


def winConditionO(gameboard):
    #vertical check for o
    winCheck_o = False
    if gameboard[0][0] == 'o' and gameboard[1][0] == 'o' and gameboard[2][0] == 'o':
        winCheck_o = True
    if gameboard[0][1] == 'o' and gameboard[1][1] == 'o' and gameboard[2][1] == 'o':
        winCheck_o = True
    if gameboard[0][2] == 'o' and gameboard[1][2] == 'o' and gameboard[2][2] == 'o':
        winCheck_o = True
    #horizontal check for o
    if gameboard[0][0] == 'o' and gameboard[0][1] == 'o' and gameboard[0][2] == 'o':
        winCheck_o = True
    if gameboard[1][0] == 'o' and gameboard[1][1] == 'o' and gameboard[1][2] == 'o':
        winCheck_o = True
    if gameboard[1][0] == 'o' and gameboard[1][1] == 'o' and gameboard[1][2] == 'o':
        winCheck_o = True
    #diagonal check for o
    if gameboard[0][0] == 'o' and gameboard[1][1] == 'o' and gameboard[2][2] == 'o':
        winCheck_o = True
    if gameboard[0][2] == 'o' and gameboard[1][1] == 'o' and gameboard[2][0] == 'o':
        winCheck_o = True

    return winCheck_o


def winConditionX(gameboard):
    #vertical check for x
    winCheck_x = False
    if gameboard[0][0] == 'x' and gameboard[1][0] == 'x' and gameboard[2][0] == 'x':
        winCheck_x = True
    if gameboard[0][1] == 'x' and gameboard[1][1] == 'x' and gameboard[2][1] == 'x':
        winCheck_x = True
    if gameboard[0][2] == 'x' and gameboard[1][2] == 'x' and gameboard[2][2] == 'x':
        winCheck_x = True
    #horizontal check for x
    if gameboard[0][0] == 'x' and gameboard[0][1] == 'x' and gameboard[0][2] == 'x':
        winCheck_x = True
    if gameboard[1][0] == 'x' and gameboard[1][1] == 'x' and gameboard[1][2] == 'x':
        winCheck_x = True
    if gameboard[1][0] == 'x' and gameboard[1][1] == 'x' and gameboard[1][2] == 'x':
        winCheck_x = True
    #diagonal check for x
    if gameboard[0][0] == 'x' and gameboard[1][1] == 'x' and gameboard[2][2] == 'x':
        winCheck_x = True
    if gameboard[0][2] == 'x' and gameboard[1][1] == 'x' and gameboard[2][0] == 'x':
        winCheck_x = True


    return winCheck_x    


def determineComputerMove(gameboard):
    if gameboard[0][0] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][2] !='x' or gameboard[1][0] != 'x' or gameboard[1][1] != 'x' or gameboard[1][2] != 'x' or gameboard[2][0] != 'x' or gameboard[2][1] != 'x' or gameboard[2][2] != 'x':
            move1 = random.randint(2,9)
            return move1
    if gameboard[0][1] == 'x':
        if gameboard[0][0] != 'x' or gameboard[0][2] !='x' or gameboard[1][0] != 'x' or gameboard[1][1] != 'x' or gameboard[1][2] != 'x' or gameboard[2][0] != 'x' or gameboard[2][1] != 'x' or gameboard[2][2] != 'x':
            move1 = random.choice(1,3,4,5,6,7,8,9)
            return move1
    if gameboard[0][2] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][0] !='x' or gameboard[1][0] != 'x' or gameboard[1][1] != 'x' or gameboard[1][2] != 'x' or gameboard[2][0] != 'x' or gameboard[2][1] != 'x' or gameboard[2][2] != 'x':
            move1 = random.choice(1,2,4,5,6,7,8,9)
            return move1
    if gameboard[1][0] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][2] !='x' or gameboard[0][0] != 'x' or gameboard[1][1] != 'x' or gameboard[1][2] != 'x' or gameboard[2][0] != 'x' or gameboard[2][1] != 'x' or gameboard[2][2] != 'x':
            move1 = random.choice(1,3,2,5,6,7,8,9)
            return move1
    if gameboard[1][1] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][2] !='x' or gameboard[1][0] != 'x' or gameboard[0][0] != 'x' or gameboard[1][2] != 'x' or gameboard[2][0] != 'x' or gameboard[2][1] != 'x' or gameboard[2][2] != 'x':
            move1 = random.choice(1,3,4,2,6,7,8,9)       
            return move1
    if gameboard[1][2] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][2] !='x' or gameboard[1][0] != 'x' or gameboard[1][1] != 'x' or gameboard[0][0] != 'x' or gameboard[2][0] != 'x' or gameboard[2][1] != 'x' or gameboard[2][2] != 'x':
            move1 = random.choice(1,3,4,5,2,7,8,9)
            return move1
    if gameboard[2][0] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][2] !='x' or gameboard[1][0] != 'x' or gameboard[1][1] != 'x' or gameboard[1][2] != 'x' or gameboard[0][0] != 'x' or gameboard[2][1] != 'x' or gameboard[2][2] != 'x':
            move1 = random.choice(1,3,4,5,6,2,8,9)
            return move1
    if gameboard[2][1] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][2] !='x' or gameboard[1][0] != 'x' or gameboard[1][1] != 'x' or gameboard[1][2] != 'x' or gameboard[2][0] != 'x' or gameboard[0][0] != 'x' or gameboard[2][2] != 'x':
            move1 = random.choice(1,3,4,5,6,7,2,9)
            return move1
    if gameboard[2][2] == 'x':
        if gameboard[0][1] != 'x' or gameboard[0][2] !='x' or gameboard[1][0] != 'x' or gameboard[1][1] != 'x' or gameboard[1][2] != 'x' or gameboard[2][0] != 'x' or gameboard[2][1] != 'x' or gameboard[0][0] != 'x':
            move1 = random.choice(1,3,4,5,6,7,8,2)
            return move1
    #checking for vertical and horizontal win conditions
    for i in range[len(gameboard)]:
        if (gameboard[i][0] == 'x' and gameboard[i][1] == 'x') or (gameboard[i][0] == 'o' and gameboard[i][1] == 'o'):
            move2 = gameboard[i][2]
            if move2 == gameboard[0][2]:
                move2 = 3
                return move2
            elif move2 == gameboard[1][2]:
                move2 = 6
                return move2
            elif move2 == gameboard[2][2]:
                move2 = 9
                return move2
            
        if (gameboard[i][1] == 'x' and gameboard[i][2] == 'x') or (gameboard[i][1] == 'o' and gameboard[i][2] == 'o'):
            move2 = gameboard[i][0]
            if move2 == [0][0]:
                move2 = 1
                return move2
            elif move2 == [1][0]:
                move2 = 4
                return move2
            elif move2 == [2][0]:
                move2 = 7
                return move2
            
        if (gameboard[i][0] == 'x' and gameboard[i][2] == 'x') or (gameboard[i][0] == 'o' and gameboard[i][2] == 'o'):
            move2 = gameboard[i][1]
            if move2 == gameboard[0][1]:
                move2 = 2
                return move2
            elif move2 == gameboard[1][1]:
                move2 = 5
                return move2
            elif move2 == gameboard[2][1]:
                move2 = 8
                return move2
        if (gameboard[0][i] == 'x' and gameboard[1][i] == 'x') or (gameboard[0][i] == 'o' and gameboard[1][i] == 'o'):
            move2 = gameboard[2][i]
            if move2 == gameboard[2][0]:
                move2 = 7
                return move2
            elif move2 == gameboard[2][1]:
                move2 = 8
                return move2
            elif move2 == gameboard[2][2]:
                move2 = 9
                return move2
        if (gameboard[0][i] == 'x' and gameboard[2][i] == 'x') or (gameboard[0][i] == 'o' and gameboard[2][i] == 'o'):
            move2 = gameboard[1][i]
            if move2 == gameboard[1][0]:
                move2 = 4
                return move2
            elif move2 == gameboard[1][1]:
                move2 = 5
                return move2
            elif move2 == gameboard[1][2]:
                move2 = 6
                return move2
                       
        if (gameboard[1][i] == 'x' and gameboard[2][i] == 'x') or (gameboard[1][i] == 'o' and gameboard[2][i] == 'o'):
            move2 = gameboard[0][i]
            if move2 == gameboard[0][0]:
                move2 = 1
                return move2
            elif move2 == gameboard[0][1]:
                move2 = 2
                return move2
            elif move2 == gameboard[0][2]:
                move2 = 3
                return move2
    #checking for diagonal win conditions
    if (gameboard[0][0] == 'x' and gameboard[1][1] == 'x') or (gameboard[0][0] == 'o' and gameboard[1][1] == 'o'):
        move2 = 9
        return move2
    if (gameboard[0][0] == 'x' and gameboard[2][2] == 'x') or (gameboard[0][0] == 'o' and gameboard[2][2] == 'o'):
        move2 = 5
        return move2
    if (gameboard[2][2] == 'x' and gameboard[1][1] == 'x') or (gameboard[2][2] == 'o' and gameboard[1][1] == 'o'):
        move2 = 1
        return move2
    if (gameboard[2][0] == 'x' and gameboard[1][1] == 'x') or (gameboard[2][0] == 'o' and gameboard[1][1] == 'o'):
        move2 = 3
        return move2
    if (gameboard[2][0] == 'x' and gameboard[0][2] == 'x') or (gameboard[2][0] == 'o' and gameboard[0][2] == 'o'):
        move2 = 5
        return move2
    if (gameboard[1][1] == 'x' and gameboard[0][2] == 'x') or (gameboard[1][1] == 'o' and gameboard[0][2] == 'o'):
        move2 = 7
        return move2
    
    else:
        running = True
        move3 = random.randint(1,9)
        while running:
            if move3 == 1 and (gameboard[0][0] == 'x' or gameboard[0][0] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 2 and (gameboard[0][1] == 'x' or gameboard[0][1] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 3 and (gameboard[0][2] == 'x' or gameboard[0][2] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 4 and (gameboard[1][0] == 'x' or gameboard[1][0] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 5 and (gameboard[1][1] == 'x' or gameboard[1][1] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 6 and (gameboard[1][2] == 'x' or gameboard[1][2] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 7 and (gameboard[2][0] == 'x' or gameboard[2][0] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 8 and (gameboard[2][1] == 'x' or gameboard[2][1] == 'o'):
                move3 = random.randint(1,9)
            elif move3 == 2 and (gameboard[2][2] == 'x' or gameboard[2][2] == 'o'):
                move3 = random.randint(1,9)
            else:
                return move3

def main():
    gameboard = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']]
    human_computer = input("Choose if you want to play with a [h]uman or a [c]omputer: ")
    if human_computer == 'h':
        player_turn = 'player1'
        running = True
        while running:
            if player_turn == 'player1':
                print(gameboard[0])
                print(gameboard[1])
                print(gameboard[2])
                move = input("Player1, what tile[1-9] do you want to convert to an x: ")
                if move == '1':
                    if gameboard[0][0] == 'o' or gameboard[0][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][0] = 'x'
                        player_turn = 'player2'
                elif move == '2':
                    if gameboard[0][1] == 'o' or gameboard[0][1] == 'x':
                        print("choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][1] = 'x'
                        player_turn = 'player2'
                elif move == '3':
                    if gameboard[0][2] == 'o' or gameboard[0][2] == 'x':
                        print("Choose a valid move as indicated by the gamebaord")
                    else:
                        gameboard[0][2] = 'x'
                        player_turn = 'player2'
                elif move == '4':
                    if gameboard[1][0] == 'o' or gameboard[1][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][0] = 'x'
                        player_turn = 'player2'
                elif move == '5':
                    if gameboard[1][1] == 'o' or gameboard[1][1] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][1] = 'x'
                        player_turn = 'player2'
                elif move == '6':
                    if gameboard[1][2] == 'o' or gameboard[1][2] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][2] = 'x'
                        player_turn = 'player2'
                elif move == '7':
                    if gameboard[2][0] == 'o' or gameboard[2][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][0] = 'x'
                        player_turn = 'player2'
                elif move == '8':
                    if gameboard[2][1] == 'o' or gameboard[2][1] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][1] = 'x'
                        player_turn = 'player2'
                elif move == '9':
                    if gameboard[2][2] == 'o' or gameboard[2][2] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][2] = 'x'
                        player_turn = 'player2'
                else:
                    print("Choose a valid move as indicated by the gameboard")
                win_check_x = winConditionX(gameboard)
                draw_checker = drawCondition(gameboard)
                if win_check_x == True:
                    print("Player 1 wins")
                    print(gameboard[0])
                    print(gameboard[1])
                    print(gameboard[2])
                    running = False
                if draw_checker == True:
                    print("It's a draw")
                    print(gameboard[0])
                    print(gameboard[1])
                    print(gameboard[2])
                    running = False
            elif player_turn == 'player2':
                print(gameboard[0])
                print(gameboard[1])
                print(gameboard[2])
                move = input("Player2, what tile[1-9] do you want to convert to an o: ")
                if move == '1':
                    if gameboard[0][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][0] = 'o'
                        player_turn = 'player1'
                elif move == '2':
                    if gameboard[0][1] == 'x':
                        print("choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][1] = 'o'
                        player_turn = 'player1'
                elif move == '3':
                    if gameboard[0][2] == 'x':
                        print("Choose a valid move as indicated by the gamebaord")
                    else:
                        gameboard[0][2] = 'o'
                        player_turn = 'player1'
                elif move == '4':
                    if gameboard[1][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][0] = 'o'
                        player_turn = 'player1'
                elif move == '5':
                    if gameboard[1][1] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][1] = 'o'
                        player_turn = 'player1'
                elif move == '6':
                    if gameboard[1][2] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][2] = 'o'
                        player_turn = 'player1'
                elif move == '7':
                    if gameboard[2][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][0] = 'o'
                        player_turn = 'player1'
                elif move == '8':
                    if gameboard[2][1] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][1] = 'o'
                        player_turn = 'player1'
                elif move == '9':
                    if gameboard[2][2] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][2] = 'o'
                        player_turn = 'player1'
                else:
                    print("Choose a valid move as indicated by the gameboard")
                win_check_o = winConditionO(gameboard)
                if win_check_o == True:
                    print("Player 2 wins")
                    print(gameboard[0])
                    print(gameboard[1])
                    print(gameboard[2])
                    running = False

    elif human_computer == 'c':
        running = True
        player_turn = 'player1' 
        while running:
            if player_turn == 'player1':
                print(gameboard[0])
                print(gameboard[1])
                print(gameboard[2])
                move = input("Player1, what tile[1-9] do you want to convert to an x: ")
                if move == '1':
                    if gameboard[0][0] == 'o' or gameboard[0][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][0] = 'x'
                        player_turn = 'player2'
                elif move == '2':
                    if gameboard[0][1] == 'o' or gameboard[0][1] == 'x':
                        print("choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][1] = 'x'
                        player_turn = 'player2'
                elif move == '3':
                    if gameboard[0][2] == 'o' or gameboard[0][2] == 'x':
                        print("Choose a valid move as indicated by the gamebaord")
                    else:
                        gameboard[0][2] = 'x'
                        player_turn = 'player2'
                elif move == '4':
                    if gameboard[1][0] == 'o' or gameboard[1][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][0] = 'x'
                        player_turn = 'player2'
                elif move == '5':
                    if gameboard[1][1] == 'o' or gameboard[1][1] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][1] = 'x'
                        player_turn = 'player2'
                elif move == '6':
                    if gameboard[1][2] == 'o' or gameboard[1][2] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][2] = 'x'
                        player_turn = 'player2'
                elif move == '7':
                    if gameboard[2][0] == 'o' or gameboard[2][0] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][0] = 'x'
                        player_turn = 'player2'
                elif move == '8':
                    if gameboard[2][1] == 'o' or gameboard[2][1] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][1] = 'x'
                        player_turn = 'player2'
                elif move == '9':
                    if gameboard[2][2] == 'o' or gameboard[2][2] == 'x':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][2] = 'x'
                        player_turn = 'player2'
                else:
                    print("Choose a valid move as indicated by the gameboard")
                win_check_x = winConditionX(gameboard)
                draw_checker = drawCondition(gameboard)
                if win_check_x == True:
                    print("Player 1 wins")
                    print(gameboard[0])
                    print(gameboard[1])
                    print(gameboard[2])
                    running = False
                if draw_checker == True:
                    print("It's a draw")
                    print(gameboard[0])
                    print(gameboard[1])
                    print(gameboard[2])
                    running = False
            elif player_turn == 'player2':
                move = determineComputerMove(gameboard)
                if move == 1:
                    gameboard[0][0] == 'o'
                    player_turn = 'player1'
                elif move == 2:
                    gameboard[0][1] == 'o'
                    player_turn = 'player1'
                elif move == 3:
                    gameboard[0][2] == 'o'
                    player_turn = 'player1'
                elif move == 4:
                    gameboard[1][0] == 'o'
                    player_turn = 'player1'
                elif move == 5:
                    gameboard[1][1] == 'o'
                    player_turn = 'player1'
                elif move == 6:
                    gameboard[1][2] == 'o'
                    player_turn = 'player1'
                elif move == 7:
                    gameboard[2][0] == 'o'
                    player_turn = 'player1'
                elif move == 8:
                    gameboard[2][1] == 'o'
                    player_turn = 'player1'
                elif move == 9:
                    gameboard[2][2] == 'o'
                    player_turn = 'player1'
                

                




if __name__ == "__main__":
    main()