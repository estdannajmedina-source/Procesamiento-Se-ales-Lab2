# Convolución, correlación y transformada de Fourier 

## Asignatura

Procesamiento Digital de Señales

## Programa

Ingeniería Biomédica – Universidad Militar Nueva Granada

## Práctica de laboratorio

**Convolución, correlación y transformada de Fourier**

## Integrantes

Danna Jimena Medina Ríos – Código 5600923
María José Polo Tovar – Código 5600894

---

## Descripción

Este informe presenta el desarrollo y análisis de la convolución, correlación y transformada de fourier aplicadas a señales discretas y biológicas. Incluye el cálculo manual y en Python, la caracterización estadística en el dominio del tiempo y el análisis espectral en el dominio de la frecuencia.

---
## Metodología
El desarrollo del laboratorio se dividió en tres partes principales.
En la primera parte, se realizó el cálculo de la convolución entre dos secuencias discretas, tanto de forma manual como mediante Python, junto con su representación gráfica. En la segunda parte, se determinó la correlación cruzada entre dos señales sinusoidales y se analizó su comportamiento. Finalmente, se generó, capturó y digitalizó una señal biológica para su caracterización estadística en el dominio del tiempo y su análisis espectral mediante la transformada de fourier.

### Parte A
En esta parte se calculó la convolución entre una señal de entrada y un sistema discreto definidos a partir de datos personales. El procedimiento se realizó de forma manual mediante sumatorias.
<p align="center">
  <img src="PARTE-A-MANUAL.png" width="700">
</p>

<p align="center">
  <em>Convolucion Parte A </em> 
</p>
Posteriormentese implementó el procedimiento en Python con el objetivo de, verificar los resultados obtenidos de ambas maneras, automatizar el cálculo y representar gráficamente la señal resultante.
Se definieron dos señales discretas:
x[n] y h[n], Ambas señales se almacenan como arreglos (array), lo que permite realizar operaciones matemáticas de manera eficiente.

```python
h = np.array([5,6,0,0,9,2,3,5,6,0,0,8,9,4])
x = np.array([1,0,2,9,1,4,3,2,6,4,1,1,0,6,2,2,7,7,8,9])
```
La convolucion se realizó mediante:

```python
y = np.convolve(x, h)
```

Esta operacion se refiere a

<p align="center">
  <img src="formulaconvolucion.png" width="700">
</p>

<p align="center">
  <em> Formula Convolucion</em> 
</p>
el proceso consiste en invertir la señal ℎ[n], desplazarla sobre x[n], multiplicar punto a punto y sumar los productos obtenidos. El resultado es una nueva señal  y[n], cuya longitud está dada por
<p align="center">
  <img src="formulal.png" width="700">
</p>

<p align="center">
  <em> Formula longitud</em> 
</p>
Para mostrar la secuencia resultante de forma organizada se utilizó:

```python
print(", ".join(map(str, y)))
```
Esto convierte cada elemento del arreglo en texto y los muestra separados por comas, facilitando la comparación con el cálculo manual.
Se creó el vector  `n = np.arange(len(y))` para representar los valores n del eje horizontal, correspondientes a cada muestra de la señal resultante.

Se utilizó la función `stem()` para graficar la señal discreta, representa cada muestra como un impulso vertical y `figsize=(14,4)` ampliar el eje horizontal para mejorar la visualización.

### Parte B
En esta parte se analizaron dos señales discretas definidas a partir de funciones trigonométricas. El objetivo fue calcular la correlación cruzada entre ambas señales para analizar el grado de similitud entre ellas cuando una se desplaza respecto a la otra.

Las señales fueron definidas utilizando una frecuencia de 100 Hz y un período de muestreo $$T_s=1.25ms$$. A partir de estos parámetros se generaron dos secuencias discretas: $x_1[n]$ y $x_2[n]$, correspondientes a una función coseno y una función seno respectivamente.

En Python, las señales se definieron de la siguiente manera:
```python
Ts = 0.00125
f = 100
n = np.arange(0,9)

w = 2*np.pi*f*Ts

x1 = np.cos(w*n)
x2 = np.sin(w*n)
```
Estas expresiones corresponden matemáticamente a:
<div align="center">

$$
x_1[n] = \cos(2\pi 100 n T_s)
$$

$$
x_2[n] = \sin(2\pi 100 n T_s)
$$

</div>
<p align="center">
  <img src="PARTE-A-MANUAL.png" width="700">
</p>

<p align="center">
<b>Figura 1. Señal discreta $x_1[n]$</b>
</p>
