"""
entrada
KM-->float-->KM
salida
Pago-->float-->P
Total-->float-->T
Total1-->float-->T1
"""
KM=int(input("Ingrese Kilometros recorridos: "))
if(KM>0 and KM<300):
	P=50000
	print("Cliente debe pagar: $ {:.0f}".format(P))
elif(KM>300 and KM<1000):
	T=(KM%100)*100000
	print("Cliente debe pagar: $ {:.0f}".format(T))
elif(KM>1000):
	T1=(((KM-1000)*9000)+150000)
	print("Cliente debe pagar: $ {:.0f}".format(T1))
else:
	print("No debe pagar nada")

