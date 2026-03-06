import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#%% Parte A
# Señales
h = np.array([5,6,0,0,9,2,3,5,6,0,0,8,9,4])
x = np.array([1,0,2,9,1,4,3,2,6,4,1,1,0,6,2,2,7,7,8,9])

N = len(h)
M = len(x)
L = N + M - 1
print("Longitud de h(n) =", N)
print("Longitud de x(n) =", M)
print("Longitud de y(n) =", L)

# Convolución
y = np.convolve(x, h)
# Valores separados por comas
print("y[n] =")
print(",".join(map(str, y)))

# Ejes de tiempo
nh = np.arange(len(h))
nx = np.arange(len(x))
ny = np.arange(len(y))

# Gráfica h[n]
plt.figure(figsize=(10,4))
plt.stem(nh, h,  linefmt='b-', markerfmt='bo', basefmt='k-')
plt.title("Señal h[n]")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.xticks(np.arange(0, len(h), 1))
plt.yticks(np.arange(0, max(h)+1, 1))
plt.grid(True)
plt.show()

# Gráfica x[n]
plt.figure(figsize=(10,4))
plt.stem(nx, x, linefmt='m-', markerfmt='mo', basefmt="k-")
plt.title("Señal x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.xticks(np.arange(0, len(x), 1))
plt.yticks(np.arange(0, max(x)+1, 1))
plt.grid(True)
plt.show()

# Gráfica y[n]
plt.figure(figsize=(10,4))
plt.stem(ny, y, linefmt='g-', markerfmt='go', basefmt="k-")
plt.title("Convolución y[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.xticks(np.arange(0, len(y), 1))
plt.yticks(np.arange(0, max(y)+20, 20))
plt.grid(True)
plt.show()

#%% Parte B
# Parámetros
Ts = 0.00125          # Periodo de muestreo
f = 100               # Frecuencia en Hz
n = np.arange(0, 9)   # 0 <= n < 9

# Frecuencia angular discreta
w = 2 * np.pi * f * Ts
print("Frecuencia angular w =", w)

# Definición de señales

x1 = np.cos(w * n)
x2 = np.sin(w * n)

print("\nValores de x1[n]:")
print(np.round(x1, 4))

print("\nValores de x2[n]:")
print(np.round(x2, 4))

# Correlación cruzada
r = np.correlate(x1, x2, mode='full')

# Vector de retardos
k = np.arange(-(len(x1)-1), len(x1))

print("\nValores de la correlación r[k]:")
print(np.round(r, 4))

# Encontrar máximo
k_max = k[np.argmax(r)]
print("\nEl valor máximo ocurre en k =", k_max)

# x1[n]
plt.figure(figsize=(8,4))
plt.stem(n, x1, linefmt='red', markerfmt='ro', basefmt='k-')
plt.title("Señal x1[n] = cos(pi n / 4)")
plt.xlabel("n")
plt.ylabel("x1[n]")
plt.grid(alpha=0.4)
plt.show()


# x2[n]
plt.figure(figsize=(8,4))
plt.stem(n, x2, linefmt='darkorange', markerfmt='o', basefmt='k-')
plt.title("Señal x2[n] = sin(pi n / 4)")
plt.xlabel("n")
plt.ylabel("x2[n]")
plt.grid(alpha=0.4)
plt.show()


# Correlación cruzada
plt.figure(figsize=(8,4))
plt.stem(k, r, linefmt='deeppink', markerfmt='o', basefmt='k-')
plt.title("Correlación cruzada r_{x1x2}[k]")
plt.xlabel("k")
plt.ylabel("r[k]")
plt.grid(alpha=0.4)
plt.show()
#%%Parte C
# CARGAR ARCHIVO
ruta_archivo = r"C:/Users/Usuario/Downloads/Procesamiento de señales/lab 2/senal_eog.txt"

datos = np.loadtxt(ruta_archivo, skiprows=1)

t = datos[:, 0]       # Columna tiempo
senal = datos[:, 1]   # Columna voltaje

fs = 300  # Frecuencia de muestreo usada en la adquisición
N = len(senal)
print("Número de muestras:", N)

# FRECUENCIA DE NYQUIST
fD =30
f_nyquist = fD * 2
print("Frecuencia de Nyquist:", f_nyquist, "Hz")

fmuestreo= 4*f_nyquist
print("Frecuencia de Muestreo:",fmuestreo, "Hz") # SE UTILIZO POR ENCIMA DE ESO

# ESTADÍSTICAS
media = np.mean(senal)
mediana = np.median(senal)
desv_std = np.std(senal)
maximo = np.max(senal)
minimo = np.min(senal)

print("\n--- Estadísticas ---")
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desv_std)
print("Máximo:", maximo)
print("Mínimo:", minimo)

# GRÁFICA EN EL TIEMPO
plt.figure(figsize=(16,4))
plt.plot(t, senal)
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Señal EOG ")
plt.grid()
plt.show()

# TRANSFORMADA DE FOURIER
frecuencias = np.fft.fftfreq(N, 1/fs)
fft_senal = np.fft.fft(senal)

magnitud = np.abs(fft_senal) / N

plt.figure(figsize=(12,5))
plt.plot(frecuencias[:N//2], magnitud[:N//2], linewidth=1)

plt.grid(True, alpha=0.3)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.title("Transformada de Fourier de la señal EOG")

plt.xlim(0, fs/2)

# ampliar escala para ver frecuencias pequeñas
plt.ylim(0, np.max(magnitud[1:N//2])*1.5)

plt.tight_layout()
plt.show()

# TRANSFORMADA DE FOURIER 
frecuencias = np.fft.fftfreq(N, 1/fs) 
fft_senal = np.fft.fft(senal) 
plt.figure(figsize=(12, 5)) 
plt.plot(frecuencias, magnitud, linewidth=1) 
plt.grid(True, alpha=0.3) 
plt.xlabel("Frecuencia (Hz)", fontsize=12) 
plt.ylabel("Magnitud", fontsize=12) 
plt.title("Transformada de Fourier de la señal EOG", fontsize=14) 
plt.xlim([0, fs/2]) 
plt.tight_layout() 
plt.show()

# DENSIDAD ESPECTRAL DE POTENCIA
frecs, psd = signal.welch(senal, fs, nperseg=512)
plt.figure(figsize=(12,4))
plt.semilogy(frecs, psd)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad Espectral de Potencia")
plt.title("Densidad Espectral - Señal EOG")
plt.grid()
plt.show()

# ESTADÍSTICOS EN DOMINIO DE FRECUENCIA

# Frecuencia media
freq_media = np.sum(frecs * psd) / np.sum(psd)
print("\nFrecuencia media:", freq_media, "Hz")

# Frecuencia mediana
psd_acumulada = np.cumsum(psd)
psd_total = psd_acumulada[-1]
indice_mediana = np.where(psd_acumulada >= psd_total/2)[0][0]
freq_mediana = frecs[indice_mediana]
print("Frecuencia mediana:", freq_mediana, "Hz")

# Desviación estándar de frecuencia
freq_std = np.sqrt(np.sum(((frecs - freq_media)**2) * psd) / np.sum(psd))
print("Desviación estándar de frecuencia:", freq_std, "Hz")


# HISTOGRAMA

plt.figure(figsize=(12,4))

plt.hist(frecs, bins=40, weights=psd,
         color="royalblue",
         edgecolor="black",
         alpha=0.8)

# Línea de la media
plt.axvline(freq_media,
            color='red',
            linestyle='dashed',
            linewidth=2,
            label=f"Media = {freq_media:.2f} Hz")

plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia acumulada")
plt.title("Histograma de distribución de potencia por frecuencia")

plt.legend()
plt.grid()

plt.show()