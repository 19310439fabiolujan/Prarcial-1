tupla_colores = ('marron', 'azul', 'negro', 'naranja')
print(tupla_colores)
colores = input('Introduce un color:\n')


if colores in tupla_colores[0]:
	print('El color marron esta admitido')
elif colores in tupla_colores[1]:
	print('El color azul esta admitido')
elif colores in tupla_colores[2]:
	print('El color negro esta admitido')
elif colores in tupla_colores[3]:
	print('El color naranja esta admitido')
else:
	print('Color no admitido')
