def ejercicio5():
    courses = ["Arquitectura y diseño de sistemas seguros", "Manejo de accesos e identidad", "Manejo de riesgos e introducción a la criptografía"]
    approved = list()
    ampli = list()
    reproved = list()
    for j in range(len(courses)):
        score = input("Que nota sacaste en " + '"' +courses[j] + '": ')
        if int(score) > 70:
            approved.append(courses[j] + "\n")
        elif (int(score) >= 60 and int(score) <= 69):
            ampli.append(courses[j] + "\n")
        else:
            reproved.append(courses[j] + "\n")
    print("\n1. Materias aprobadas: " + lenList(approved) + "\n" + "2. Materias ampliación: " + lenList(ampli) + "\n" + "3. Materias reprobadas: " + lenList(reproved))

def lenList(nameList):
    if len(nameList) == 0:
        result = str(0) + "\n"
    else:
        result = "".join(nameList)
    return result

ejercicio5()


