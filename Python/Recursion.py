'''this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']
def feeding(this_list):
    if len(this_list) == 1:
        this_list = this_list[0]
        print("The " + this_list + " has been fed")
    else:
        mid = len(this_list) // 2
        first_half = this_list[:mid]
        second_half = this_list[mid:]
        feeding(first_half)
        feeding(second_half)
feeding(this_list)'''

'''books = [int(n) for n in input("Input a list of numbers").split()]
def idkwhatthepointis(books):
    if len(books) == 2:
        print(books[0] + books[1])
    else:
        mid = len(books) // 2
        idkwhatthepointis(books[:mid])
        idkwhatthepointis(books[mid:])
idkwhatthepointis(books)'''

flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]
def orchard(flowers):
    if len(flowers) == 1:
        print(flowers[0] * 3, end = ' ')
    else:
        mid = len(flowers) // 2
        orchard(flowers[:mid])
        orchard(flowers[mid:])
orchard(flowers)