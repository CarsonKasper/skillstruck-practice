# Code Check
#rows = 5
#cols = 3
#list = []
#for i in range(rows):
#    col = []
#    for j in range(cols):
#        col.append(5)
#    list.append(col)
#print(list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Challenge 1
#first = ['Carson', 'Avery', 'Kinsley', 'Jackson']
#last = ['Kasper', 'Smith', 'Andrew', 'Krysten']
#Combo = []

# One Line Nested For Loop
#Combo = [[i + ' ' + j for i in first] for j in last]

#Standared Nested For Loop
#for i in first:
#    list = []
#    for j in last:
#        list.append(i + ' ' + j)
#    Combo.append(list)
#print(Combo)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Challenge 2
flavors = ["apple", "grape", "peach", "cinnamon", "vanilla"]
fruits = input('Name some fruits').split()
FruitCombo = [[i + ' ' + j for j in flavors] for i in fruits]
print(FruitCombo)