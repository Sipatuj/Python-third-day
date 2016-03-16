import random

words = input('Введите слово ')
word = words

drow = ''
while word:
	position = word[len(word)-1]
	drow += position
	word = word[0:len(word)-1]
	
print(drow)
	