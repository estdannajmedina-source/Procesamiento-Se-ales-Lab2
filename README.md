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
En primer lugar, se realizó la representación gráfica de las señales x[n] de forma manual. Para ello se tomaron los valores de cada secuencia y se construyeron sus respectivas graficas, donde cada muestra se representa mediante una línea vertical terminada en un punto. Esta representación permitió visualizar el comportamiento discreto de las señales y ubicar correctamente cada valor respecto al índice n. 

$$h(n) =[5,6,0,0,9,2,3,5,6,0,0,8,9,4]$$

$$x(n) =[1,0,2,9,1,4,3,2,6,4,1,1,0,6,2,2,7,7,8,9]$$
<p align="center">
  <img src="señales.jpeg" width="700">
</p>

<p align="center">
  <em>Señales</em> 
</p>


Posteriormente, se determinó la longitud de las señales involucradas en el sistema. La señal h[n] corresponde a la respuesta del sistema y está formada por 14 muestras, mientras que la señal x[n] corresponde a la señal de entrada y contiene 20 muestras. A partir de estos valores se calculó la longitud de la señal resultante y[n] De esta forma se obtuvo que la señal resultante tiene 33 muestras. Se realizó el cálculo de la convolución de forma manual utilizando la definición matemática de la convolución discreta $$y[n]=∑x[k]h[n−k].$$ Este procedimiento consiste en calcular la convolución de forma manual utilizando una tabla. En esta tabla se organizaron los desplazamientos de la señal h[n] respecto a la señal x[n], realizando las multiplicaciones entre los valores correspondientes en cada posición. Posteriormente se sumaron los productos obtenidos en cada desplazamiento para calcular cada valor de la señal resultante y[n]. Este método permitió visualizar de manera ordenada el proceso de convolución y facilitar el cálculo de cada término de la secuencia resultante. Tambien se grafico la señal y[n] resultante.
<p align="center">
  <img src="PARTE-A-MANUAL.jpeg" width="700">
</p>
<p align="center">
  <em>Convolucion Parte A </em> 
</p>

<p align="center">
  <img src="GRAFICA-FINAL .jpeg" width="700">
</p>
<p align="center">
  <em>GRAFICA A MANO</em> 
</p>

Posteriormentese implementó el procedimiento en Python con el objetivo de, verificar los resultados obtenidos de ambas maneras, automatizar el cálculo y representar gráficamente la señal resultante.
Se definieron dos señales discretas en phyton: x[n] y h[n], Ambas señales se almacenan como arreglos (array),lo que permite realizar operaciones matemáticas de manera eficiente y ademas se graficaron.

```python
h = np.array([5,6,0,0,9,2,3,5,6,0,0,8,9,4])
x = np.array([1,0,2,9,1,4,3,2,6,4,1,1,0,6,2,2,7,7,8,9])
```
<p align="center">
  <img src="HN.png" width="700">
</p>
<p align="center">
  <em>H[n]</em> 
</p>

<p align="center">
  <img src="XN.png" width="700">
</p>

<p align="center">
  <em>X[n]</em> 
</p>

La convolucion se realizó mediante:

```python
y = np.convolve(x, h)
```
y se procedio a graficar

<p align="center">
  <img src="YN.png" width="700">
</p>

<p align="center">
  <em>Y[n]</em> 
</p>

Para mostrar la secuencia resultante de forma organizada se utilizó:

```python
print(", ".join(map(str, y)))
```
<p align="center">
  <img src="L .png" width="700">
</p>

<p align="center">
  <em>Señal Y[n]</em> 
</p>
Esto convierte cada elemento del arreglo en texto y los muestra separados por comas, facilitando la comparación con el cálculo manual.

Se creó el vector `np.arange(len(y))` para representar los valores n del eje horizontal, correspondientes a cada muestra de la señal resultante.

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

$$
x_1[n] = \cos(2\pi 100 n T_s)
$$

$$
x_2[n] = \sin(2\pi 100 n T_s)
$$

<p align="center">
  <img src="XN1.png" width="700">
</p>

<p align="center">
   <em>Señal discreta x<sub>1</sub>[n]</em>
</p>

<p align="center">
<img src="XN2.png" width="700">
</p>

<p align="center">
    <em>Señal discreta x<sub>2</sub>[n]</em>
</p>

Posteriormente se calculó la correlación cruzada, la cual permite medir la similitud entre dos señales cuando una de ellas se desplaza en el tiempo. Esta operación es ampliamente utilizada en procesamiento digital de señales para identificar retardos o coincidencias entre señales.

En Python, la correlación se calculó mediante la función:
```python
r = np.correlate(x1, x2, mode='full')
```
El resultado de esta operación es una nueva secuencia $$r[k]$$ que representa la correlación entre las dos señales para distintos valores de desplazamiento. Para representar los retardos en el eje horizontal se definió el siguiente vector:
```python
k = np.arange(-(len(x1)-1), len(x1))
```
Finalmente, para visualizar el comportamiento de la correlación cruzada se utilizó la función stem(), la cual permite representar señales discretas mediante impulsos verticales, facilitando la interpretación de cada muestra.

<p align="center">
  <img src="CORRELACION.png" width="700">
</p>

<p align="center">
   <em>Correlación cruzada r<sub>x₁x₂</sub>[k]</em>
</p>

A partir de la gráfica obtenida se observa que la correlación presenta un valor máximo cuando  $$k=2$$. Esto indica que las señales presentan mayor similitud cuando una de ellas se desplaza dos muestras respecto a la otra. Este comportamiento se debe a que las funciones seno y coseno poseen un desfase de 90°, lo cual se refleja en el desplazamiento observado en la correlación.

De esta manera, el análisis confirma que la correlación cruzada es una herramienta útil para estudiar la relación entre señales discretas y detectar retardos entre ellas.
