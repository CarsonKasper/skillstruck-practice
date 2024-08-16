'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person('Jasmine', '15', 'Female')
p2 = Person('George', '67', 'Male')

print('Person 1: ' + p1.name + ' ' + p1.age + ' ' + p1.gender)
print('Person 2: ' + p2.name + ' ' + p2.age + ' ' + p2.gender)
'''

'''
class Hat:
    def __init__(self, kind, color, material):
        self.kind = kind
        self.color = color
        self.material = material

myObject = Hat('Cowbow', 'Red', 'Leather')
print('Hat: ' + myObject.kind + ' ' + myObject.color + ' ' + myObject.material)
'''
'''
class Fruit:
    def __init__(self, shape, kind, size):
        self.shape = shape
        self.kind = kind
        self.size = size

f1 = Fruit('1', '2', '3')
f2 = Fruit('1', '2', '3')
f3 = Fruit('1', '2', '3')
f4 = Fruit('1', '2', '3')

print(f1.kind)
print(f2.kind)
print(f3.kind)
print(f4.kind)
'''

class Pet:
    def __init__(self, i, d, k):
        self.i = i
        self.d = d
        self.k = k

c = Pet(1, 2, 3)
h = Pet(1, 2, 3)
m = Pet(1, 2, 3)