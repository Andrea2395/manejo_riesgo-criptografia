price = input("Ingresar el precio del producto con dos decimales: ")
splitPrice = price.split(".")
print(splitPrice[0] + " colones y " + splitPrice[1] + " cèntimos.")