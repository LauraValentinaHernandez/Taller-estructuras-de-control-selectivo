"""
entrada
cantidada-->float-->C
tasa-->float-->T  
tasa%-->float-->TP
salida
intereses-->float-->I
salarioneto-->float-->ST
"""
C=float(input("Digite cantidad que tiene en inversión en el banco: "))
T=float(input("Escriba la tasa de interes: "))
TP=T/100
I=(C*TP)
if(I>100000):
  ST=C+I
  print("Intereses exceden a $100.000: Reinvertir intereses")
  print("Salario neto es igual: "+str(ST))
else:
  ST=C+I
  print("Intereses NO exceden a $100.000: NO reinvertir intereses")
  print("Salario neto es igual: "+str(ST))
