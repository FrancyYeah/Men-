import os # es una libreria para ocupar comandos de consola
#import numpy as np # numpy es una libreria de matematica 

from datetime import datetime
import time 
### menu options and defie

menu = {}
menu['1']= "reproducir un tema aleatorio"
menu['2']= "frase desmotivacional"
menu['3']= "numero al azar"
menu['4']= "recomendación de genero musical"
menu['5']= "salir \n"
while True:
	print( 'welcome son of the earth')
	print('')
	options = menu.keys()
	options = sorted(options)
	#options.sort
	for entry in options:
		print (entry, menu[entry])

	selection=input("seleccione opcion : ")
	if selection =='1':
		lista_temas= ['tiburones en el bosque zorros en el mar','lose yourself', 'mario neta', 'la bala','stressedout','lovers on the sun','the nights', 'country roads take me home', 'gangsta paradise']
		variable_1 = input('elija un numero entre 1 y 9 : ')
     
		### pasar una funcion
		os.system('clear')
		now = datetime.now()
		current_time = str(now.strftime("%H:%M:%S"))
		print('la variable ingresada en la opcion 1 del menu es: {}'.format(lista_temas[int(variable_1)-1]),current_time)
		time.sleep(0.1)

	elif selection == '2':
		variable_2 = input('ingrese una variable : ')

		os.system('clear')
		now = datetime.now()
		current_time = str(now.strftime("%H:%M:%S"))
		print('la variable ingresada en la opcion 2 del menu es: {}'.format(variable_2),current_time)
		time.sleep(0.1)

	elif selection == '3':
		variable_3 = input('ingrese una variable : ')

		os.system('clear')
		now = datetime.now()
		current_time = str(now.strftime("%H:%M:%S"))
		print('la variable ingresada en la opcion 3 del menu es: {}'.format(variable_3),current_time)
		time.sleep(0.1)

	elif selection == '4':
		variable_4 = input('ingrese una variable : ')

		os.system('clear')
		now = datetime.now()
		current_time = str(now.strftime("%H:%M:%S"))
		print('la variable ingresada en la opcion 4 del menu es: {}'.format(variable_4),current_time)
		time.sleep(0.1)

	elif selection == '5':
		break
	else:
		os.system('clear')
		print('numero ingresado no valido')
