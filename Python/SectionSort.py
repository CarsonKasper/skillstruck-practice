number = int(input('Give Number'))
lst = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
lst.append(number)
for i in range(len(lst)):
    minimum = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[minimum]:
            minimum = j
    if minimum != i:
        lst[i], lst[minimum] = lst[minimum], lst[i]
print(lst)