import random
a = random.randint(1, 200)
for i in range(1, random.randint(1, a)):
    print(random.randint(1, 6), i, 'this is reasonable')
print('total amount of loops')
print(a)
