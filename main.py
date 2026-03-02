print("#." * 9)
print("Adivina el numero")
print("#." * 9)

numerosecreto = 7

while True:
	try:
		adivinanza = int(input("Adivina el numero del 1 al 10: "))
		if adivinanza == numerosecreto:
			print("CORRECTO, adivinaste el numero")
			break
			
		else:
			print("INCORRECTO, sigue intentandolo")
	except ValueError:
		print("Introduce por favor un numero valido")