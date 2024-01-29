import pandas as pd
import numpy as np

# Función para calcular la luminosidad a partir de la relación de Tully-Fisher
def tully_fisher_relation(Vmax, alpha, A):
    return A * (Vmax)**alpha

# Función para convertir magnitud aparente y luminosidad en distancia
def distance_from_luminosity(m, L):
    # Convertir luminosidad a magnitud absoluta
    M = -2.5 * np.log10(L)
    # Calcular la distancia usando la fórmula de módulo de distancia
    distance = 10**((m - M + 5) / 5) / 1e6  # Convertir de parsecs a Mpc
    return distance

# Leer los datos del archivo CSV
df = pd.read_csv('tully_fisher_cal.csv')

# Pedir al usuario el nombre de la galaxia
galaxy_name = input("Introduce el nombre de la galaxia: ")

# Encontrar la galaxia en el dataframe
galaxy_data = df[df['Name'].str.strip() == galaxy_name]

# Si la galaxia no se encuentra en el dataframe, terminar el script
if galaxy_data.empty:
    print(f"No se encontró la galaxia {galaxy_name} en el archivo.")
    exit()

# Pedir al usuario los parámetros de la relación de Tully-Fisher
alpha = float(input("Introduce el valor de alpha: "))
A = float(input("Introduce el valor de A: "))

# Obtener los valores necesarios de la galaxia
Vmax = galaxy_data['Vmax'].values[0]
m_spitzer = galaxy_data['m_spitzer'].values[0]
distance_known = galaxy_data['Distance'].values[0]

print(f"Datos de {galaxy_name}:")
print(f"Vmax: {Vmax}")
print(f"m_spitzer: {m_spitzer}")
print(f"Distancia en la tabla: {distance_known}")

# Calcular la luminosidad y la distancia estimada
L = tully_fisher_relation(Vmax, alpha, A)
distance_estimated = distance_from_luminosity(m_spitzer, L)

# Mostrar los resultados
print(f"Distancia estimada para {galaxy_name}: {distance_estimated:.2f} Mpc")
print(f"Distancia conocida para {galaxy_name}: {distance_known:.2f} Mpc")
print(f"Diferencia: {abs(distance_estimated - distance_known):.2f} Mpc")

