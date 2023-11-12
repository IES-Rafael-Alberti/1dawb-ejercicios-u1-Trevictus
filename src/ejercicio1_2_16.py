barraPan = 3.49
barraPasada = barraPan*0.6
descuento = barraPan - barraPasada
barraComprada = int(input("¿Cuantas barras pasadas has comprado? "))

print("El precio de una barra de pan es", barraPan, ", el descuento que se le hace a las barras no frescas es", round(descuento,2), "y el coste total de las barras que no son del día compradas es de:",round(barraComprada*barraPasada, 2))