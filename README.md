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
Posteriormente en Python, incluyendo la representación gráfica y secuencial de la señal resultante, esto se elaboro mediante,
```python
directory = r"C:/Users/Usuario/Downloads/Procesamiento de señales/LAB 1/"
record = wfdb.rdsamp(os.path.join(directory, "ath_001"))
```
