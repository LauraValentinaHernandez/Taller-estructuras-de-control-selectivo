"""
Entradas
numero de estudiantes--->int--->est
numero de mujeres-->int--->numm
numero de hombres--->int--->numh

Salidas
Porcentaje de hombres--->float--->ph
porcentaje de mujeres--->float--->pm
"""
est=int(input("Introduzca el número de estudiantes: "))
numm=int(input("¿Cuantas mujeres hay en el grupo? "))
numh=int(est-numm)
ph=((numh/est)*100)
pm=((numm/est)*100)
print("El porcentaje de mujeres es: "+str(pm))
print("El porcentaje de hombres es: "+str(ph))