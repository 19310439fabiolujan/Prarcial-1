#!/usr/bin/env python
# _*_ coding: cp1252 _*_ 
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_


# Valor inicial de x
x = 0

# while se ejecuta hasta menor o igual que 30
while x <= 30:
	x += 1  # incrementos de 1

	# if para saltar ejecuciones del bucle
	if x == 4 or x == 6 or x == 10:
		print('Se salt? el valor ', x, ' de x')
		continue

	# if para romper la ejecuci?n del bucle
	if x == 15:
		print('Se rompi? la ejecuci?n del bucle cuando x val?a: ', x)
		break

	# imprime los resultados que no se corresponden a ninguno de los if
	print(x)