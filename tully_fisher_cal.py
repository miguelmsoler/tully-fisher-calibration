import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df = pd.read_csv('tully_fisher_cal.csv')

# Calcular magnitud absoluta y luminosidad
M_sun = 3.26 # IRAC 3.6um vegamag
df['M'] = df['m_spitzer'] - 5 * np.log10(df['Distance'] * 1e6) + 5
df['L'] = 10 ** ((M_sun - df['M']) / 2.5)

# Tomar logaritmos
df['logVmax'] = np.log10(df['Vmax'])
df['logL'] = np.log10(df['L'])

# Definir función para ajustar
def tully_fisher(logVmax, alpha, logA):
    return logA + alpha * logVmax

# Ajustar modelo
popt, pcov = curve_fit(tully_fisher, df['logVmax'], df['logL'])
alpha, logA = popt
A = 10 ** logA

# Convertir a arreglos de NumPy para el trazado
logVmax_np = df['logVmax'].to_numpy()
logL_np = df['logL'].to_numpy()

# Graficar
plt.scatter(logVmax_np, logL_np, label='Datos')
plt.plot(logVmax_np, tully_fisher(logVmax_np, *popt), color='red', label=f'Ajuste: alpha={alpha:.2f}, A={A:.2e}')

plt.xlabel('log(Vmax) [log(km/s)]')
plt.ylabel('log(L) [log(L/L_sun)]')
plt.legend()
plt.title('Calibración de la Relación de Tully-Fisher')
plt.show()

# Imprimir resultados
print(f'alpha ajustado: {alpha:.2f}')
print(f'A ajustado: {A:.2e}')
