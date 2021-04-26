"""
entrada
piezas-->int-->P
costo-->float--C
salida
total-->int-->T
inversion-->int-->I
banco-->int-->B
credito-->int-->C
intereses-->int-->IN
"""
P=int(input("Digite numero de piezas: "))
C=int(input("Digite costo por pieza: "))
T=P*C
if(T>5000000):
  I=T*0.55
  B=T*0.30
  C=T*0.15
  IN=C*0.20
  print("Total del propio dinero: $ {:.1f}".format(I))
  print("Total prestamo al banco: $ {:.1f}".format(B))
  print("Total intereses fabricante: $ {:.1f}".format(IN))
  print("Total credito fabricante con intereses: $ {:.1f}".format(C+IN))
elif(T>0 and T<5000000):
  I=T*0.70
  C=T*0.30
  IN=C*0.20
  print("Total del propio dinero: $ {:.1f}".format(I))
  print("Total intereses fabricante: $ {:.1f}".format(IN))
  print("Total credito fabricante con intereses: $ {:.1f}".format(C+IN))
else:
	print("Error al digitar")

