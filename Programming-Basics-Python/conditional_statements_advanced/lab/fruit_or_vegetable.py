product = input()

fruits = 'banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'
vegetables = 'tomato', 'cucumber', 'pepper', 'carrot'

result = ''
if product in fruits:
    result = 'fruit'
elif product in vegetables:
    result = 'vegetable'
else:
    result = 'unknown'

print(result)
