nivel=int(input("Digite nvel de hemoglobina: "))
año=int(input("Digite año: "))
sexo=("Digite sexo: ")
mes=año/12
if(mes<=1 and nivel<13):
	print("Positivo")
elif(mes>1 and mes<=6 and nivel>=10 and nivel<18):
	print("Positivo")
elif(mes>6 and mes<=12 and nivel>=11 and nivel<15):
	print("Positivo")
elif(año>1 and año<=5 and nivel>=11.5 and nivel<15):
	print("Positivo")
elif(edad>5 and edad<=10 and nivel>=12.6 and nivel<15.5):
	print("Positivo")
elif(edad>10 and edad<=15 and nivel>=13 and nivel<15.5):
	print("Positivo")
else:
  print("Negativo")
  



