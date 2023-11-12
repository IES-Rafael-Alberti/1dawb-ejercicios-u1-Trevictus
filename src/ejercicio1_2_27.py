producto = input("Introduce el nombre del producto: ")
precio = input("Introduce su coste: ")
unidades= input("Nº de u del producto: ")
total= unidades* precio
print(f"{producto} {precio: 6.2f} {unidades: 03d} {total: 8.2f}")