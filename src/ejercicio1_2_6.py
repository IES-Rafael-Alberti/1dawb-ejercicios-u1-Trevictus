importeFinal = float(input("Introduzaca el importe total del articulo: "))
iva = float(input("Introduzca el porcentaje de iva que conlleva su producto: "))
print("El importe sin iva que ha pagado por el articulo es: ",importeFinal-(importeFinal*(iva/100)))
print("El valor del iva del producto que paga es: ",(iva/100)*importeFinal)