coins = {
    'pennies' : 0,
    'nickels' : 0,
    'dimes' : 0,
    'quarters' : 0,
}

coins['silver dollar'] = 1
coins.pop('pennies')

print(coins)
print(len(coins))