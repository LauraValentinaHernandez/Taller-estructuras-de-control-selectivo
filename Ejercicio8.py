"""
Dados como datos los valores enteros P y Q, determine si los mismos satisfacen la siguiente expresión: P3 + Q4 – 2*P2 > 680. En caso afirmativo debe mostrar los valores de “P y Q satisfacen la expresión”, de lo contrario muestre un mensaje “P y Q no Satisfacen la expresión”. Utilice la concatenación para mostrar los valores
"""
P=int(input("Ingrese dato uno: "))
Q=int(input("Ingrese dato dos: "))
if((P**3)+(Q**4)-(2*(P**2))>680):
	print("Los valores que satisfacen la expresión son: " + ' {} y {}'.format(P, Q))
else:
	print("P y Q no satisfacen la expresión")