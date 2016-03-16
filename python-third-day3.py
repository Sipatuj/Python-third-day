message = input('Введите слово: ')
print('Длина слова ',len(message)," символов")
print( "\nСамая частая согласная . 'o' . ")
if 'o' in message:
	print("встречается в вашем тексте.")
else:
	print("не встречается в вашем тексте.")