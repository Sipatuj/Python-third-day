import random 

WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

word = random.choice(WORDS)

correct = word

jumble = ''

while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word =word[:position] + word[(position+1):]

print ('''Добро пожаловать в игру 'Анаграммы'!
Надо переставить буквы так. чтобы получилось осмысленное слово.
(Для выхода нажмите Enter. не вводя своей версии.)''')

print("Boт анаграмма:",jumble)

gest = input('введите ваше слово ')
while gest != correct and gest != '':
	print('Вы не угадали')
	gest = input('введите ваше слово ')
if gest == correct:
	print('Поздравляю вы угадали!')
