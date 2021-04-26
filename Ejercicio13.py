"""
Desarrolle un algoritmo que reciba como dato de entrada la fecha de nacimiento de una persona y a continuación escriba el nombre del signo del zodiaco correspondiente; así como su edad. Considere la siguiente tabla de signos:
"""
dia=int(input("Digite día de nacimiento: "))
mes=int(input("Digite mes de nacimiento: "))
año=int(input("Digite año de nacimiento: "))
edad=2021-año
if(dia>=22 and mes==11) or (dia<=21 and mes==12):
	Signo="Sagitario"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=22 and mes==12) or (dia<=20 and mes==1):
	Signo="Capricornio"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=21 and mes==1) or (dia<=19 and mes==2):
	Signo="Acuario"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=20 and mes==2) or (dia<=19 and mes==3):
	Signo="Piscis"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=21 and mes==3) or (dia<=20 and mes==4):
	Signo="Aries"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=21 and mes==4) or (dia<=19 and mes==5):
	Signo="Tauro"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=22 and mes==5) or (dia<=21 and mes==6):
	Signo="Geminis"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=22 and mes==6) or (dia<=22 and mes==7):
	Signo="Cancer"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=23 and mes==7) or (dia<=23 and mes==8):
	Signo="Leo"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=24 and mes==8) or (dia<=22 and mes==9):
	Signo="Virgo"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=23 and mes==9) or (dia<=22 and mes==10):
	Signo="Libra"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
elif(dia>=23 and mes==10) or (dia<=21 and mes==11):
	Signo="Escorpion"
	print("Su signo zodiacal es: " +str(Signo))
	print("Su edad es: " +str(edad) +" años")
else:
	print("ERROR")