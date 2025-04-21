import pandas as pd

# Crear un DataFrame simple
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 34, 45, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame inicial:")
print(df)

# Filtrar filas donde la edad sea mayor a 30
filtro = df[df['Edad'] > 30]
print("\nFiltrar filas donde la edad sea mayor a 30:")
print(filtro)

# Agregar una nueva columna
df['Puntaje'] = [85, 90, 78, 88]
print("\nDataFrame con nueva columna 'Puntaje':")
print(df)

# Guardar el DataFrame en un archivo CSV
df.to_csv('output.csv', index=False)
print("\nEl DataFrame se ha guardado en 'output.csv'.")

# Leer el archivo CSV
df_leido = pd.read_csv('output.csv')
print("\nDataFrame leído desde 'output.csv':")
print(df_leido)