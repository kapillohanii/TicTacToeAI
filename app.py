from flask import Flask, request, jsonify, render_template
import numpy as np


app = Flask(__name__)

def isboardfull(board):
  for i in range(1,10):
    if isspacefree(board,i):
      return False
  return True

def isspacefree(board,index):
  return board[index]==' '

def iswinner(board,letter):
  return ((board[1]==letter and board[2]==letter and board[3]==letter) or
			(board[4]==letter and board[5]==letter and board[6]==letter) or
			(board[7]==letter and board[8]==letter and board[9]==letter) or
			(board[1]==letter and board[4]==letter and board[7]==letter) or
			(board[2]==letter and board[5]==letter and board[8]==letter) or
			(board[3]==letter and board[6]==letter and board[9]==letter) or
			(board[1]==letter and board[5]==letter and board[9]==letter) or
			(board[3]==letter and board[5]==letter and board[7]==letter))

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
  
  bestval = -1000
  bestmove = -1
  for i in range(0,9):
    if isspacefree(board,i):
      board[i] = computerletter
      moveval = MiniMax(board,0,False,-1000,1000,computerletter)
      board[i]= ' '
      if moveval > bestval:
        bestmove = i
        bestval = moveval
  
  return bestmove

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_computer_move', methods=['POST'])
def get_computer_move():
    data = request.get_json()
    
    # Extract the board state from the received data
    board_state = data['board']
    #move = data['move']
    print(board_state)
    # Use the unbeatable Tic Tac Toe AI to find the best move
    # (You'll need to integrate this logic with your existing AI code)
    computer_move = findbestmove(board_state, 'O')

    # Return the computer's move as a JSON response
    response = {'move': computer_move}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
