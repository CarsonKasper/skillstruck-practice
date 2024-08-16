#rows = int(input('How many rows?'))
#mylist = [1, 2, 3, 4, 5]
#numbers = [[i * rows for i in mylist] for j in range(rows)]
#print(numbers)
wind = ["windy", "breezy", "calm"]
weather = input("Input a list of weather").split()
condition = [[i + ' ' + j for j in wind] for i in weather]
print(condition)