"""
entrada
sueldo-->int-->S
ventas1-->float--V1
ventas2-->float--V2
ventas3-->float--V3
salida
ventatotal-->float-->VT 
cumplimiento-->float--> C
sueldofinal-->float-->SF
"""
S=int(input("Digite sueldo bruto mensual: "))
V1=int(input("Digite ventas realizadas por departamento 1: "))
V2=int(input("Digite ventas realizadas por departamento 2: "))
V3=int(input("Digite ventas realizadas por departamento 3: "))
VT=V1+V2+V3
C=VT*0.33
if(V1>C):
  SF=((S*0.20)+S)
  print("Total salario departamento 1 + incentivo : "+str(SF))
else:
  print("Total salario departamento 1: "+str(S))
if(V2>C):
  SF=((S*0.20)+S)
  print("Total salario departamento 2 + incentivo : "+str(SF))
else:
  print("Total salario departamento 2: "+str(S))
if(V3>C):
  SF=((S*0.20)+S)
  print("Total salario departamento 3 + incentivo : "+str(SF))
else:
  print("Total salario departamento 3: "+str(S))


