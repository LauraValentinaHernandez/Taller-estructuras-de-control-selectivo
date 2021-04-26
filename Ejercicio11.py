"""
Desarrolle un algoritmo, que dado como dato una temperatura en grados Fahrenheit, determine el deporte que es apropiado practicar a esa temperatura, teniendo en cuenta la siguiente tabla:
"""
T=float(input("Digite la temperatura: "))
if(T>85):
  print("Deporte que es apropiado practicar a esa temperatura: Natación")
elif(T>=71 and T<=85):
  print("Deporte que es apropiado practicar a esa temperatura: Tenis")
elif(T>=33 and T<=70):
  print("Deporte que es apropiado practicar a esa temperatura: Golf")
elif(T>=11 and T<=32):
  print("Deporte que es apropiado practicar a esa temperatura: Esquí")
elif(T<=10):
  print("Deporte que es apropiado practicar a esa temperatura: Marcha")
else:
  print("Deporte que es apropiado practicar a esa temperatura: No se identifico deporte")  