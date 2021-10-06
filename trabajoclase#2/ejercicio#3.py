def ejercicio3():
    numList = list()
    minimum = None
    maximum = None
    for x in range(10):
        num = input("Ingrese un número: ")
        numList.append(num)
    minimum = min(numList, key=int)
    maximum = max(numList, key=int)
    print("El número mayor es : " + maximum + " y el número menor es: " + minimum)

ejercicio3()