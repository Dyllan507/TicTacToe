#Dyllan Spooner          11/03/25

#Making a tictactoe game through lists in python


def drawCondition(gameboard):
    drawCheck = False
    for i in range(len(gameboard)):
        for j in range(len(gameboard)):
            if gameboard[i][j] == 'o' or gameboard[i][j] == 'x':
                if i == 2 and j == 2: 
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
            win_check_o = winConditionO(gameboard)
            draw_checker = drawCondition(gameboard)
            if win_check_x == True:
                print("Player 1 wins")
                running = False
            if win_check_o == True:
                print("Player 2 wins")
                running = False
            if draw_checker == True:
                print("It's a draw")
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
            win_check_x = winConditionX(gameboard)
            win_check_o = winConditionO(gameboard)
            draw_checker = drawCondition(gameboard)
            if win_check_x == True:
                print("Player 1 wins")
                running = False
            if win_check_o == True:
                print("Player 2 wins")
                running = False
            if draw_checker == True:
                print("It's a draw")
                running = False
                
                




if __name__ == "__main__":
    main()