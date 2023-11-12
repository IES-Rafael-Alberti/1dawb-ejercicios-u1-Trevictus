precioProducto= float(input("Introduce el precio del producto con dos decimales: "))
euros = int(precioProducto)
centimos = int((precioProducto-euros) *100)


print(euros,"euros", centimos,"centimos.")