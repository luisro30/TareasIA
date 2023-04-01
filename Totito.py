import random
 
def drawBoard(board):

    # la siguiente función nos sirve para hacer el tablero de nuestro jueggo.
 
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
 
def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Desea ser X o O?')
        letter = input().upper()
 
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def whoGoesFirst():

    # En la siguiente función haremos como si lanzaramos una moneda
    # con la finalidad de elegir si el jugador o la computadora 
    # va a empezar con el juego

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
def playAgain():

    print('Desea jugar otra vez? (si o no)')
    return input().lower().startswith('s')
 
def makeMove(board, letter, move):
    board[move] = letter
 
def isWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le))
 
def getBoardCopy(board):
    
    dupeBoard = []
 
    for i in board:
        dupeBoard.append(i)
 
    return dupeBoard
 
def isSpaceFree(board, move):
    
    return board[move] == ' '
 
def getPlayerMove(board):
    
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('en qué casilla colocará su siguiente marca? (1-9)')
        move = input()
    return int(move)
 
def chooseRandomMoveFromList(board, movesList):

    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
 
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
 
    if isSpaceFree(board, 5):
        return 5
 
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
 
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
 
 
print('Bienvenido a Totito')
print('La forma de colocar sus marcas es la siguiente:')
print('las casillas están asignadas del 1-9, así que para ubicarse')
print('empezamos desde la 1 en parte inferior izquierda hacia la derecha')
print('luego la 4 en la parte media izquierda, y la 7 en la superior izquierda ')
print('Buena suerte ganándole al computador y que lo disfrutes :D')
 
while True:
    
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('El ' + turn + ' Empieza')
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'player':
      
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
 
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Has ganado')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empate')
                    break
                else:
                    turn = 'computer'
 
        else:
            
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
 
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Te ganó la compu xd')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empate')
                    break
                else:
                    turn = 'player'
 
    if not playAgain():
        break