import random

word = input('Введите слово: ')
print(' В переменной word хранится слово ',word)
hign = len(word)
low = -len(word)
for x in range(10):
	position = random.randrange(low, hign)
	print('word[',position,']\t',word[position])