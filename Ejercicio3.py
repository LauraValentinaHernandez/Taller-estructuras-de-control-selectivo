"""
entrada
A-->int-->a
B-->int-->b
C-->int-->c
D-->int-->DeprecationWarning
salida
resultadofinal-->float-->RF
"""
a=int(input("Digite dato A: "))
b=int(input("Digite dato B: "))
c=int(input("Digite dato C: "))
d=int(input("Digite dato D: "))
if(d<=0):
  RF=((a-c)**2)
  print("Resultado si el dato D es = 0: "+str(RF))
elif(d>0):
  RF=(((a-b)**3)/d)
  print("Resultado si el dato D es > 0: "+str(RF))
