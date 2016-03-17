'''
1)комп загадує слово і сообщає скільки там букв
2) 5 попиток щоб узнати букву
3) і останнє це угадати саме слово

'''
import random 

WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

word = random.choice(WORDS)
print('Компютер загадал слово')
print('У вас только 5 попыток чтоб отгадать слово ')
print('В слове ',len(word),' букв')

i = 4
dor = input('Назовите вашу букву ')
while i!=0:
	for item in word:
		if item == dor:
			print('Итеррация',item)
			print('da')
	i -= 1
	dor = input('Назовите вашу букву ')


gest = input('введите ваше слово ')
while gest != word and gest != '':
	print('Вы не угадали')
	gest = input('введите ваше слово ')
if gest == word:
	print('Поздравляю вы угадали!')