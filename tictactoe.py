# Tic-Tac-Toe CSE 210 Programming with classes. Author- Francisco Franco

print('Welcome, this is tic-tac-toe. Let us see if you can win.\n')


def main():

    board = ['1','2','3',
            '4','5','6',
            '7','8','9']
    game = True
    drawBoard(board)
    print()

    while game: 
        playGame(board)
        

def drawBoard(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-+-+-')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-+-+-')
    print(board[6]+'|'+board[7]+'|'+board[8])


def playGame(board):
    insertMark_x = int(input('X Enter a number from 1-9 to take a place: '))
    if insertMark_x >= 1 and insertMark_x <= 9 and board[insertMark_x-1] in board: 
        board[insertMark_x-1] = 'x'
        drawBoard(board) 
    else : 
        print('That place is already filled, please choose another number')
        insertMark_x = int(input('X Enter a number from 1-9 to take a place: '))
        board[insertMark_x-1] = 'x'
        drawBoard(board) 

    insertMark_o = int(input('O Enter a number from 1-9 to take a place: '))
    if insertMark_o >= 1 and insertMark_o <= 9 and board[insertMark_o-1] != 'x' and board[insertMark_o-1] in board: 
        board[insertMark_o-1] = 'o'
        drawBoard(board)  
    else : 
        print('That place is already filled, please choose another number')
        insertMark_o = int(input('O Enter a number from 1-9 to take a place: '))
        board[insertMark_o-1] = 'o'
        drawBoard(board)  


        



    
        
    



if __name__ == '__main__':
    main()

