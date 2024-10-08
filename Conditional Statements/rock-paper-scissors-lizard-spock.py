player1 = str(input())
player2 = str(input())

if (player1 == 'scissors') and (player2 == 'paper' or player2 == 'lizard'):
    print('player1 wins')
elif (player1 == 'paper') and (player2 == 'rock' or player2 == 'Spock'):
    print('player1 wins')
elif (player1 == 'rock') and (player2 == 'scissors' or player2 == 'lizard'):
    print('player1 wins')
elif (player1 == 'Spock') and (player2 == 'scissors' or player2 == 'rock'):
    print('player1 wins')
elif (player1 == 'lizard') and (player2 == 'Spock' or player2 == 'paper'):
    print('player1 wins')
elif player1 == player2:
    print('draw')
else:
    print('player2 wins')
    