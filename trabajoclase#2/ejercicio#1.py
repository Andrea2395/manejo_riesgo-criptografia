def ejercicio1():
    asignatura = None
    lista = list()
    
    while asignatura != '0':
        asignatura = input("Ingrese nombre de asignatura (0 para salir): ")
        if asignatura != '0':
            lista.append(asignatura)
            
    print(lista)
    
    
ejercicio1()