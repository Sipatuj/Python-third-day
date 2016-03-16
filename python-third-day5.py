ivent = ()
if not ivent:
	print('Вы безоружны ')
input("\nHaжмитe Enter. чтобы продолжить.")

ivent = ('меч',
		 'щит',
		 'кольчуга',
		 'лук',
		 'стелы')
print('Подобрано ')
print(ivent)

print('И так в нашем арсенале ')
for x in ivent:
	print(x)
