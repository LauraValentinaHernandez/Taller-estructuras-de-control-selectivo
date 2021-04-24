  
"""
entradas
salariobruto-->float--sb
salida
salarioneto-->float--sn
"""
sb=float(input("Digite salario bruto: "))
if(sb<900000):
  sf=sb+(sb*0.15)
  print("Salario neto es igual: "+str(sf))
else:
  sf=sb+(sb*0.12)
  print("Salario neto es igual: "+str(sf)) 

  