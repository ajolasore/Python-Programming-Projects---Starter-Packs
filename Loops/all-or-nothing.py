# Read the initial capital
initial_capital = int(input())
current_capital = initial_capital

while True:
    bet_amount = input()

    if (bet_amount == "stop") or (current_capital == 0):
        # Player chooses to stop
        print("You end up with {} dollar.".format(current_capital))
        break

    if bet_amount == "all":
        bet_amount = current_capital
    else:
        bet_amount = int(bet_amount)

    bet_color = input()
    ball_color = input()

    if bet_amount > current_capital:
        # Player cannot bet more than their current capital
        print("You cannot bet {} dollar if you only have {} dollar.".format(bet_amount, current_capital))
        break

    if bet_color == ball_color:
        current_capital += bet_amount
    else:
        current_capital -= bet_amount

# End of the game
