name = input("Introduce el nombre del producto: ")
price = int(input("Introduce el precio unitario: "))
num = int(input("Introduce el nùmero de unidades: "))
print(name + ": " + str(num) + " unidades x " + str(price) + " = " + str(price * num))