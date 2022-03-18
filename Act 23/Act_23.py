

edad = int(input('Cual es tu edad\n'))

if edad <= 0:
	print('Nadie puede tener esa edad')


elif edad <= 1 and edad < 18:
	print('Eres menor de edad')

elif edad == 18 and edad <= 45:
	print('Estas dentro de 18 a 45')

elif edad > 100 and edad <= 120:
	print('Eres INMORTAL')

else:
	print('Edad no valida')
