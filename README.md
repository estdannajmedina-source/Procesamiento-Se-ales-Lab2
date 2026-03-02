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
En la primera parte, se realizó el cálculo de la convolución entre dos secuencias discretas, tanto de forma manual como mediante Python, junto con su representación gráfica. En la segunda parte, se determinó la correlación cruzada entre dos señales sinusoidales y se analizó su comportamiento. Finalmente, se generó, capturo y digitalizó una señal biológica para su caracterización estadística en el dominio del tiempo y su análisis espectral mediante la Transformada de Fourier.

### Parte A
En esta sección se calculó la convolución entre una señal de entrada y un sistema discreto definidos a partir de datos personales. El procedimiento se realizó de forma manual mediante sumatorias.
<p align="center">
  <img src="PARTE-A-MANUAL.png" width="700">
</p>

<p align="center">
  <em>Convolucion Parte A </em> 
</p>
Posteriormentese implementó el procedimiento en Python con el objetivo de:
*Verificar los resultados obtenidos manualmente.
*Automatizar el cálculo de la operación.
*Representar gráficamente la señal resultante.

Se definieron dos señales discretas:
x[n] → Señal de entrada.
h[n] → Respuesta al impulso del sistema.
Ambas señales se almacenan como arreglos (array) de NumPy, lo que permite realizar operaciones matemáticas de forma eficiente.
```python
h = np.array([5,6,0,0,9,2,3,5,6,0,0,8,9,4])
x = np.array([1,0,2,9,1,4,3,2,6,4,1,1,0,6,2,2,7,7,8,9])
```
La convolucion se realizó mediante:
```python
y = np.convolve(x, h)
```

