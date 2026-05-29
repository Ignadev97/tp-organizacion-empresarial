import pandas as pd

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Calculos estadisticos
total_ventas = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
venta_maxima = df["sales_amount"].max()
venta_minima = df["sales_amount"].min()
cantidad_registros = len(df)

# Guardar resultados
with open("resultados/resumen_ventas.txt", "w") as archivo:
    archivo.write("RESUMEN DE VENTAS\n")
    archivo.write("-------------------\n")
    archivo.write(f"Total ventas: {total_ventas}\n")
    archivo.write(f"Promedio ventas: {promedio_ventas}\n")
    archivo.write(f"Venta maxima: {venta_maxima}\n")
    archivo.write(f"Venta minima: {venta_minima}\n")
    archivo.write(f"Cantidad registros: {cantidad_registros}\n")

print("Analisis completado correctamente")
