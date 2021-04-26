"""
Se tienen 4 dígitos en las variables A, B, C, D que forman un entero positivo N. Se desea redondear N a la centena más próxima y mostrar el resultado. Considere los siguientes ejemplos: Si A es 2, B es 3, C es 6 y D es 2, entonces N es 2362 y el resultado redondeado es 2400. Si N es 2342, el resultado redondeado será 2300 y si N es 2962, el resultado redondeado será 3000.
"""
A=int(input("Ingrese primer digito: ")) #Miles
B=int(input("Ingrese segundo digito: ")) #Centenas
C=int(input("Ingrese tercer digito: ")) #decenas
D=int(input("Ingrese cuarto digito: ")) #unidades
if (C>=5):
	A1=A*1000
	B1=B*100
	N=A1+(B1+100)
	print(N)
else:
	A2=A*1000
	B2=B*100
	N=A2+B2
	print(N)


