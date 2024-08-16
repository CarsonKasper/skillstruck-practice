#my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]

#number = int(input('What Number?'))
#rows = 4
#cols = 3

#for i in range(rows):
    #for a in range(cols):
        #my_list[i][a] *= number
#print(my_list)

x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
z = int(input("What is the third number?"))
my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]

rows = 4
cols = 3
biggest = 0

for i in range(rows):
    for a in range(cols):
        if biggest < my_list[i][a]:
            biggest = my_list[i][a] 
print(biggest)

# This is the way smarter way to do it instead of this stuipid for loop method# ~~ print(max(max(my_list)))