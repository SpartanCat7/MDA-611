from Lector_de_Datos import Lector_de_Datos

import numpy as np

lector = Lector_de_Datos()

lista_datos_entrada = lector.leer_de_json("datos_normalizados.txt")
lista_datos_salida = lector.leer_personalidades_de_json("datos_normalizados.txt")

datos_salida = []
for dato in lista_datos_salida:
    if (dato.lower() == "optimista"):
        datos_salida.append(1)
    else:
        datos_salida.append(0)
    
print("Datos leidos")
print(datos_salida)
print(lista_datos_entrada[0])

datos_entrada_ascii = []
for respuesta_encuesta in lista_datos_entrada:
    nueva_respuesta_encuesta = []
    for respuesta_pregunta in respuesta_encuesta:
        nueva_respuesta_pregunta = []
        for palabra in respuesta_pregunta:
            nueva_palabra = []
            for caracter in palabra:
                nueva_palabra.append(ord(caracter))
            nueva_respuesta_pregunta.append(nueva_palabra)
        nueva_respuesta_encuesta.append(nueva_respuesta_pregunta)
    datos_entrada_ascii.append(nueva_respuesta_encuesta)

print("Datos convertidos a ASCII")

datos_entrada_float = []
for respuesta_encuesta in datos_entrada_ascii:
    nueva_respuesta_encuesta = []
    for respuesta_pregunta in respuesta_encuesta:
        nueva_respuesta_pregunta = []
        for palabra in respuesta_pregunta:
            nueva_palabra = []
            for caracter in palabra:
                nueva_palabra.append(float(caracter))
            nueva_respuesta_pregunta.append(nueva_palabra)
        nueva_respuesta_encuesta.append(nueva_respuesta_pregunta)
    datos_entrada_float.append(nueva_respuesta_encuesta)

print("Datos convertidos a Float")

max_encuestas = len(datos_entrada_float)
max_respuestas = 0
max_palabras = 0
max_letras = 0
for encuesta in datos_entrada_float:
    if(len(encuesta) > max_respuestas):
        max_respuestas = len(encuesta)
    for respuesta in encuesta:
        if(len(respuesta) > max_palabras):
            max_palabras = len(respuesta)
        for palabra in respuesta:
            if(len(palabra) > max_letras):
                max_letras = len(palabra)

print("max_encuestas: " + str(max_encuestas))
print("max_respuestas: " + str(max_respuestas))
print("max_palabras: " + str(max_palabras))
print("max_letras: " + str(max_letras))

X = np.ndarray((max_encuestas,max_respuestas,max_palabras,max_letras),float)
for i, encuesta in enumerate(datos_entrada_float):
    for j, respuesta in enumerate(encuesta):
        for k, palabra in enumerate(respuesta):
            for l, letra in enumerate(palabra):
                #print(str(i) + "-" + str(j) + "-" + str(k) + "-" + str(l))
                X[i][j][k][l] = letra

#X = np.array(datos_entrada_float)
Y = np.array(datos_salida)
print("X[0]")
print(X[0])


import tensorflow as tf

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
    )
print(datos_entrada_float[0])

model.fit(X,Y,epochs=3)

model.save('modelo.h5')