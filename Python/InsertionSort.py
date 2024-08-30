number = int(input('Give Number'))
lst = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
lst.append(number)
for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and key < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key
print(lst)