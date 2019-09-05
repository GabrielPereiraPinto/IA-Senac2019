import random
import math
    
def duplicateBoard(board):
    duplicate = []

    for i in board:
        duplicate.append(i)

    return duplicate

def printBoard(board):
    duplicate = duplicateBoard(board)

    for i in range(1,10):
        if(board[i] == ' '):
            duplicate[i] = str(i)
        else:
            duplicate[i] = board[i]

    print(' ' + duplicate[1] + ' | ' + duplicate[2] +  ' | ' + duplicate[3])
    print('------------')
    print(' ' + duplicate[4] + ' | ' + duplicate[5] +  ' | ' + duplicate[6])
    print('------------')
    print(' ' + duplicate[7] + ' | ' + duplicate[8] +  ' | ' + duplicate[9])
    print('------------ \n')

def isPositionFree(board, position):
    return (board[position] == ' ')

def isBoardFull(board):
    for i in range(1,10):
        if isPositionFree(board, i):
            return False 
        
    return True

def getPosition(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not isPositionFree(board, int(position)):
        print('Digite uma posição:')
        position = input()

    return int(position)

def setPosition(board, symbol, position):
    board[position] = symbol

def delSymbol(board, position):
    board[position] = ' '

def getPossiblePositions(board):
    possiblePositions = []
    for i in range(1,10):
        if isPositionFree(board, i):
            possiblePositions.append(i)
        
    return possiblePositions

def checkWinner(board, winner):
    return( 
            (board[1] == winner and board[2] == winner and board[3] == winner) or 
            (board[4] == winner and board[5] == winner and board[6] == winner) or
            (board[7] == winner and board[8] == winner and board[9] == winner) or
            (board[1] == winner and board[4] == winner and board[7] == winner) or
            (board[2] == winner and board[5] == winner and board[8] == winner) or
            (board[3] == winner and board[6] == winner and board[9] == winner) or
            (board[1] == winner and board[5] == winner and board[9] == winner) or
            (board[3] == winner and board[5] == winner and board[7] == winner)       
        )

def getPlayerSymbol(compSymbol):
    if compSymbol == 'X':
        return 'O'
    else:
        return 'X'

def endGame(board, compSymbol):

    playerSymbol = getPlayerSymbol(compSymbol)
    
    if(checkWinner(board, compSymbol)):
        return -1
    elif(checkWinner(board, playerSymbol)):
        return 1
    elif(isBoardFull(board)):
        return 0
    else:
        return None

def minimax(board, compSymbol, playerSymbol, turn, alpha, beta):
    if turn == compSymbol: 
        nextTurn = playerSymbol
    else:
        nextTurn = compSymbol
    end = endGame(board, compSymbol)
    if end != None:
        return end
    
    possiblePosition = getPossiblePositions(board)

    if turn == compSymbol:
        for position in possiblePosition:
                setPosition(board, turn, position)
                value = minimax(board, compSymbol, playerSymbol, nextTurn, alpha, beta)
                delSymbol(board, position)

                if value > alpha:
                    alpha = value
                if beta <= alpha:
                    return alpha
                
        return alpha
    else:
        for position in possiblePosition:
            setPosition(board, turn, position)
            value = minimax(board, compSymbol, playerSymbol, nextTurn, alpha, beta)
            delSymbol(board, position)
            
            if value < beta:
                beta = value
            if beta <= alpha:
                return beta
        return beta

def checkNextPosition(compSymbol, playerSymbol, board):
    duplicate = duplicateBoard(board)

    for i in range(1,10):
        if isPositionFree(duplicate, i):
            setPosition(duplicate, compSymbol, i)
            if checkWinner(duplicate, compSymbol):
                return i
            else:
                duplicate[i] = ' '
    for i in range(1,10):
        if isPositionFree(duplicate, i):
            setPosition(duplicate, playerSymbol, i)
            if checkWinner(duplicate, playerSymbol):
                return i
            else:
                duplicate[i] = ' '
    return None

def getCompPosition(board, turn, compSymbol):
    alpha = -2
    possible = []

    playerSymbol = getPlayerSymbol(compSymbol)

    nextPosition = checkNextPosition(compSymbol, playerSymbol, board)
    if nextPosition != None:
        return nextPosition

    possible = getPossiblePositions(board)

    for position in possible:
        setPosition(board, compSymbol, position)
        value = minimax(board, compSymbol, playerSymbol,playerSymbol, -2, 2) 
        delSymbol(board, position)

        if value > alpha:
            alpha = value 
            possible = [position]
        elif value == alpha:
            possible.append(position)
    
    return random.choice(possible)

def tictactoe():
    board = [' '] * 10
    print('Escolha um simbolo entre X e O:')

    playerSymbol = ' '
    while not (playerSymbol == 'X' or playerSymbol == 'O'):
        playerSymbol = input().upper()

    if(playerSymbol == 'X'):
        compSymbol = 'O'
    else:
        compSymbol = 'X'
    
    turn = ' '
    if random.randint(0,1) == 1:
        turn = 'comp'
    else: turn = 'player'
    
    print('Primeiro turno: ' + turn)

    gameIsOn = True

    while gameIsOn:

        if turn == 'player':
            printBoard(board)
            position = getPosition(board)
            setPosition(board, playerSymbol, position)

            if checkWinner(board, playerSymbol):
                printBoard(board)
                print('Jogador venceu')
                gameIsOn = False
            else:
                if isBoardFull(board):
                    printBoard(board)
                    print('Empate')
                    gameIsOn = False
                else:
                    turn = 'comp'

        else:
            position = getCompPosition(board, playerSymbol, compSymbol)
            setPosition(board, compSymbol, position)

            if checkWinner(board, compSymbol):
                printBoard(board)
                print('Computador venceu')
                gameIsOn = False
            
            else:
                if isBoardFull(board):
                    printBoard(board)
                    print('Empate')
                    gameIsOn = False
                else:
                    turn = 'player'

tictactoe()