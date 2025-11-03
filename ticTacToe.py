#Dyllan Spooner          11/03/25

#Making a tictactoe game through lists in python


def main():
    gameboard = [
    ['1''2''3']
    ['4''5''6']
    ['7''8''9']
    ]

    human_computer = input("Choose if you want to play with a [h]uman or a [c]omputer: ")
    if human_computer == 'h':
        player_turn = 'player1'
        running = True
        while running:
            print(gameboard)
            if player_turn == 'player1':
                move = input("What tile[1-9] do you want to convert to an x: ")
                if move == '1':
                    if gameboard[0][0] == 'o':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][0] = 'x'
                        player_turn = 'player2'
                elif move == '2':
                    if gameboard[0][1] == 'o':
                        print("choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[0][1] = 'x'
                        player_turn = 'player2'
                elif move == '3':
                    if gameboard[0][2] == 'o':
                        print("Choose a valid move as indicated by the gamebaord")
                    else:
                        gameboard[0][2] = 'x'
                        player_turn = 'player2'
                elif move == '4':
                    if gameboard[1][0] == 'o':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][0] = 'x'
                        player_turn = 'player2'
                elif move == '5':
                    if gameboard[1][1] == 'o':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][1] = 'x'
                        player_turn = 'player2'
                elif move == '6':
                    if gameboard[1][2] == 'o':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[1][2] = 'x'
                        player_turn = 'player2'
                elif move == '7':
                    if gameboard[2][0] == 'o':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][0] = 'x'
                        player_turn = 'player2'
                elif move == '8':
                    if gameboard[2][1] == 'o':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][1] = 'x'
                        player_turn = 'player2'
                elif move == '9':
                    if gameboard[2][2] == 'o':
                        print("Choose a valid move as indicated by the gameboard")
                    else:
                        gameboard[2][2] = 'x'
                        player_turn = 'player2'
                else:
                    print("Choose a valid move as indicated by the gameboard")
                




main()