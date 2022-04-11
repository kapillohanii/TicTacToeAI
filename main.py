#unbeatable tic tac toe ai
import numpy as np


def drawBoard(board):
	# This function prints out the board that it was passed.
	# "board" is a list of 10 strings representing the board (ignore index 0)
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('--+---+--')
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('--+---+--')
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def inputplayerletter():
  letter = ' '
  while not(letter=='X' or letter=='O'):
    letter = input('Do you want to play as X/O?\n ').upper()
  if letter == 'X':
    return ['X','O']
  else:
    return ['O','X']
def whogoesfirst():
  print("Do you want to go first?(yes/no)")
  try:
    if input().lower().startswith('y'):
      return "player"
    else:
      return "computer"
  except:
    print("select either yes or no.")
    whogoesfirst()

def playagain():
  print("DO YOU WANT TO PLAY AGAIN? (yes/no) ")
  return input().lower().startswith('y')

def makeMove(board, letter, move):
	board[move] = letter

def iswinner(board,letter):
  return ((board[1]==letter and board[2]==letter and board[3]==letter) or
			(board[4]==letter and board[5]==letter and board[6]==letter) or
			(board[7]==letter and board[8]==letter and board[9]==letter) or
			(board[1]==letter and board[4]==letter and board[7]==letter) or
			(board[2]==letter and board[5]==letter and board[8]==letter) or
			(board[3]==letter and board[6]==letter and board[9]==letter) or
			(board[1]==letter and board[5]==letter and board[9]==letter) or
			(board[3]==letter and board[5]==letter and board[7]==letter))

def dupboard(board):
  boardcopy = np.copy(board)
  return boardcopy

def isspacefree(board,index):
  return board[index]==' '

def getplayermove(board):
  move = '' 
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not isspacefree(board,int(move)):
    print('What is your next move? (1-9)')
    move = input()
    return int(move)

def MiniMax(board,depth,isMax,alpha,beta,computerletter):
  
  if computerletter == 'X':
    playerletter = 'O'
  else:
    playerletter = 'X'
  
  if iswinner(board,computerletter):
    return 10
  if iswinner(board,playerletter):
    return -10
  if isboardfull(board):
    return 0

  if isMax:
    best = -1000
    for i in range(1,10):
      if isspacefree(board,i):
        board[i] = computerletter
        best = max(best,MiniMax(board,depth+1,not isMax,alpha,beta,computerletter) - depth)
        alpha = max(alpha,best)
        board[i] = ' '
        if alpha >= beta:
          break
    return best
  else:
    best = 1000
    for i in range(1,10):
      if isspacefree(board,i):
        board[i] = playerletter
        best = min(best,MiniMax(board,depth+1, not isMax,alpha,beta,computerletter) + depth)
        beta = min(beta,best)
        board[i] = ' '
        if alpha >= beta:
          break
    return best

def findbestmove(board,computerletter):
  if computerletter == 'X':
    playerletter = 'O'
  else:
    playerletter = 'X'
  
  bestval = -1000
  bestmove = -1
  for i in range(1,10):
    if isspacefree(board,i):
      board[i] = computerletter
      moveval = MiniMax(board,0,False,-1000,1000,computerletter)
      board[i]= ' '
      if moveval > bestval:
        bestmove = i
        bestval = moveval
  
  return bestmove

def isboardfull(board):
  for i in range(1,10):
    if isspacefree(board,i):
      return False
  return True

print("TIC TAC TOE!")
print("refrence of numbering on board")
drawBoard('0 1 2 3 4 5 6 7 8 9'.split())
print(' ')

while True:
  theboard = [' ']*10
  playerletter, computerletter = inputplayerletter()
  turn = whogoesfirst()
  print('The '+ turn + ' will go first.')

  isgameplaying = True

  while isgameplaying:
    if turn =='player':
      drawBoard(theboard)
      move = getplayermove(theboard)
      makeMove(theboard,playerletter,move)

      if iswinner(theboard,playerletter):
        drawBoard(theboard)
        print('You won the game.')
        isgameplaying = False
      else:
        if isboardfull(theboard):
          drawBoard(theboard)
          print('The game is a Tie.')
          break
        else:
          turn = 'computer'
    
    else:
      drawBoard(theboard)
      move = findbestmove(theboard,computerletter)
      makeMove(theboard,computerletter,move)

      if iswinner(theboard,computerletter):
        drawBoard(theboard)
        print('You lost.')
        isgameplaying = False
      else:
        if isboardfull(theboard):
          drawBoard(theboard)
          print('The game is a Tie.')
          break
        else:
          turn = 'player'
    
  if not playagain():
    break

      