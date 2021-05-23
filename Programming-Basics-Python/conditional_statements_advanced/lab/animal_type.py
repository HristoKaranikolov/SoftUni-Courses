animal = input()

mammals = 'dog'
reptiles = 'crocodile', 'tortoise', 'snake'

if animal in mammals:
    print('mammal')
elif animal in reptiles:
    print('reptile')
else:
    print('unknown')
