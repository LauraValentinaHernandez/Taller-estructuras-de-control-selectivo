"""
Desarrolle un programa en Python que calcule y muestre el monto que debe pagar ar suscriptor por concepto de consumo de luz eléctrica y servicio de aseo urbano. Dicho monto se calcula multiplicando la diferencia de la lectura anterior y la lectura actual por el costo de cada Kilovatio hora, según la siguiente escala:
"""
lecturanterior=int(input("Digite lectura anterior: "))
lecturactual=int(input("Digite lectura actual: "))
D=lecturactual-lecturanterior
if(D>0 and D<=100):
	totalpago=D*4.600
	print("Monto total a pagar es:  {:.0f}".format(totalpago))
elif(D>101 and D<=300):
	totalpago=D*80.00
	print("Monto total a pagar es:  {:.0f}".format(totalpago))
elif(D>301 and D<=500):
	totalpago=D*100.000
	print("Monto total a pagar es:  {:.0f}".format(totalpago))
elif(D>501):
	totalpago=D*120.000
	print("Monto total a pagar es:  {:.0f}".format(totalpago))
else:
	print("!!!ERRORRR¡¡¡¡")
