import smtplib
import random


smtp_user = 'correo@electronico'
smtp_password = 'contraseña'
server = 'smtp.gmail.com'
port = 587

diccionario_nombres = {'Nombre 1':'correo@electronicoº', 'Nombre 2':'correo@electronico', 'Nombre 3':'correo@electronico', 'Nombre 4':'correo@electronico'}
diccionario_comidas = {'Mexicana':1, 'Asiatica':2, 'Americana':3, 'India':4, 'Italiana':5, 'Griega':7}

diccionario_random = {'Nombre':'Comida'}

lista_nombres_random = random.sample(diccionario_nombres.keys(), len(diccionario_nombres))
lista_comidas_random = random.sample(diccionario_comidas.keys(), len(diccionario_nombres))


cont = 0
for nombre in lista_nombres_random:

	email = diccionario_nombres[nombre] 
	comida = lista_comidas_random[cont]

	# MENSAJE DEL CORREO   
	SUBJECT = "SORTEO DE COMIDAS - " + nombre
	TEXT = "Este correo electronico indica que comida va a traer preparada para todos tus amigos \n\n Nombre: " + nombre + "\nComida: " + comida + "\n\n\nNo olvide que tiene que presentarse con suplato en el día XX del mes XX a las XX:XX am/pm\n\nUn saludo."

	message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

 	# METODO DE ENVIO DE MENSAJE 
	s = smtplib.SMTP(server, port)
	s.ehlo()
	s.starttls()
	s.login(smtp_user, smtp_password)   
	s.sendmail(smtp_user, email, message)

 	# TERMINAR SESIÓN
	s.quit()

	# 
	print(email)
	print(comida)
	print(nombre)
	print('------')

	# AUMENTAR CONTADOR PARA QUE RECORRA LA LISTA DE LAS COMIDAS ALEATORIAS 
	cont = cont + 1