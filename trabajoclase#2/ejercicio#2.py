import string 

def ejercicio2():
    alfabeto = list(string.ascii_lowercase)
    for index in range(len(alfabeto), 1, -1):
        if index % 3 == 0:
            alfabeto.pop(index-1)

    print(alfabeto)

ejercicio2()