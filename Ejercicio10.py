  
"""
Construya un programa en Python que, dados como datos la categoría y el sueldo bruto
del trabajador, calcule el aumento correspondiente teniendo en cuenta la siguiente tabla:
Como salida, mostrar la categoría del trabajador y su nuevo sueldo bruto.
"""
SB=int(input("Digite sueldo bruto: "))
if(SB<=9000000 ):
	nsalario= (SB*0.6)+SB
	print("Nuevo salario bruto: $ {:.0f}".format(nsalario))
	print("Pertence a categoria: 5")
elif(SB>9000000 and SB<=2000000):
	nsalario= (SB*0.4)+SB
	print("Nuevo salario bruto: $ {:.0f}".format(nsalario))
	print("Pertence a categoria: 4")
elif(SB>2000000 and SB<=3600000):
	nsalario= (SB*0.2)+SB
	print("Nuevo salario bruto: $ {:.0f}".format(nsalario))
	print("Pertence a categoria: 3")
elif(SB>3600000 and SB<=4300000):
	nsalario= (SB*0.15)+SB
	print("Nuevo salario bruto: $ {:.0f}".format(nsalario))
	print("Pertence a categoria: 2")
elif(SB>4300000 and SB<=5000000):
	nsalario= (SB*0.10)+SB
	print("Nuevo salario bruto: $ {:.0f}".format(nsalario))
	print("Pertences a categoria: 1")
else:
	print("Error")