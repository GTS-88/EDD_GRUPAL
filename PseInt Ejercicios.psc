Algoritmo Examen
	//Ejercicio 1 de PseInt
	Escribir "Hoy es tu d�a puedes llevarte hasta un 23% de descuento en tu compra total para saber cual es tu % de descuento debes ingresar tu coste de la compra TOTAL para saber a cuanto te saldr�."
	Escribir "El juego consiste en que se sacar� un n�mero al azar entre el 0 y el 500 si el n�mero escogido es menor que 100 el descuento es del 10%, si es mayor o igual a 100 el descuento es del 20%. Adem�s, si el n�mero es par,  se le aplicar� un 2% adicional. Por el contrario, si es impar, se le aplicar� un 3%"
	Numeroazar=Aleatorio(0,500)
	descuento_final=0
	NumPar=PAR
	Escribir  "El n�mero que sali� fu� el " Numeroazar
	si Numeroazar >100
		descuento_final= descuento_final+20
	SiNo
		descuento_final= descuento_final+10
	FinSi
	si Numeroazar%2=0
		descuento_final= descuento_final+2
	SiNo
		descuento_final= descuento_final+3
	FinSi
	Escribir "Su descuento es de " descuento_final "%"
	Leer dineroTotal
	Escribir dineroTotal
	Escribir "El descuento es de " (dineroTotal*descuento_final)/100 "$"
	Escribir "El dinero a pagar es " dineroTotal-(dineroTotal*descuento_final)/100 "$"
	
	//Ejercicio 2 PseInt 
	Escribir "El director de la escuela necesita saber cuanto porcentaje de ni�os y ni�as hay en el curso actual"
	Escribir "Cu�ntos ni�os hay: "
	Leer Ni�os
	Escribir "Cu�ntos ni�as hay: "
	Leer Ni�as
	
	TotalDeAlumnos = Ni�os+Ni�as
	si TotalDeAlumnos = 0
		Escribir "No existe curso"
	SiNo
		PorNi�os= Trunc(Ni�os*100/TotalDeAlumnos)
		PorNi�as= trunc(Ni�as*100/TotalDeAlumnos)
	FinSi
	
	Escribir "Hay un " PorNi�os "% de ni�os" 
	Escribir "Hay un " PorNi�as "% de ni�as"
	
	si Ni�os =0
		Escribir "El porcentaje de ni�os no es par ni impar"
	SiNo
		si PorNi�os %2 = 0
			Escribir "El porcentaje de ni�os es par"
		SiNo
			Escribir "El porcentaje de ni�os es impar"
		FinSi
	FinSi
	
	si PorNi�as = 0
		Escribir "El porcentaje de ni�as no es par ni impar"
	SiNo
		si PorNi�as %2 = 0
			Escribir "El porcentaje de ni�as es par"
		SiNo
			Escribir "El porcentaje de ni�as es impar"
		FinSi
	FinSi
FinAlgoritmo
