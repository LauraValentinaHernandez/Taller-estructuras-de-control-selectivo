"""
En una tienda efectúan un descuento a los clientes dependiendo del monto de la compra.
El descuento se efectúa con base en el siguiente criterio:
a.	Si el monto es inferior a $50.000 COP, no hay descuento.
b.	Si está comprendido entre $50.000 COP y $100.000 COP inclusive,
se hace un descuento del 5%.
c.	Si está comprendido entre $100.000 COP y $700.000 COP inclusive,
se hace un descuento del 11%.
d.	Si está comprendido entre $700.000 COP y $1.500.000 COP inclusive,
el descuento es del 18.
e.	Si el monto es mayor a $1500000, hay un 25% de descuento.
Calcule y muestre el nombre del cliente, el monto de la compra, monto a pagar
y descuento recibido.
"""
N=input("Digite nombre del cliente: ")
C=int(input("Digite total de la compra: "))
if(C>0 and C<50000):
	print("Nombre del cliente: "+ str(N))
	print("Total de la compra: $ {:.0f}".format(C))
	print("No hay descuento")
	print("Monto a Pagar: $ {:.0f}".format(C))
elif(C>=50000 and C<100000):
	D=(C*0.05)
	Totalpagar=(C-D)
	print("Nombre del cliente: "+ str(N))
	print("Monto de la compra: $ {:.0f}".format(C))
	print("Descuento Recibido: $ {:.0f}".format(D))
	print("Monto a Pagar: $ {:.0f}".format(Totalpagar))
elif(C>=100000 and C<700000):
	D=(C*0.11)
	Totalpagar=(C-D)
	print("Nombre del cliente: "+ str(N))
	print("Monto de la compra: $ {:.0f}".format(C))
	print("Descuento Recibido: $ {:.0f}".format(D))
	print("Monto a Pagar: $ {:.0f}".format(Totalpagar))
elif(C>=700000 and C<1500000):
	D=(C*0.18)
	Totalpagar=(C-D)
	print("Nombre del cliente: "+ str(N))
	print("Monto de la compra: $ {:.0f}".format(C))
	print("Descuento Recibido: $ {:.0f}".format(D))
	print("Monto a Pagar: $ {:.0f}".format(Totalpagar))
elif(C>=1500000):
	D=(C*0.25)
	Totalpagar=(C-D)
	print("Nombre del cliente: "+ str(N))
	print("Monto de la compra: $ {:.0f}".format(C))
	print("Descuento Recibido: $ {:.0f}".format(D))
	print("Monto a Pagar: $ {:.0f}".format(Totalpagar))	
else:
	print("ERROR")