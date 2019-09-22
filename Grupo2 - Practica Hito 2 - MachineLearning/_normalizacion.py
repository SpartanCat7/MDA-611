
from Lector_de_Datos import Lector_de_Datos
from Manejador_de_Texto import Manejador_de_Texto
from Graficador import Graficador
from Analizador_de_Datos import Analizador_de_Datos
from Normalizar import normalizar

lector = Lector_de_Datos()
manejador = Manejador_de_Texto()
graficador = Graficador()
analizador = Analizador_de_Datos()
normalizar=normalizar()

#lector.guardar_a_json(lector.leer_de_excel("Mineria de datos.xlsx"),lector.leer_personalidades_de_excel("Mineria de datos.xlsx"),"archivo.txt")


nombre_de_lista = "lista"
nombre_de_archivo = "archivo.txt" #solo por el momento

lista_datos_original = lector.leer_de_json(nombre_de_archivo)
lista_personalidades = lector.leer_personalidades_de_json(nombre_de_archivo)

#print(lista_datos_original)
#print(lista_personalidades)
# Formato: [
#   ["Respuesta A1","Respuesta A2","Respuesta A3"],
#   ["Respuesta B1","Respuesta B2","Respuesta B3"],
#   ["Respuesta C1","Respuesta C2","Respuesta C3"],
#   ["Respuesta D1","Respuesta D2","Respuesta D3"] ]

#creo que sera un poco complicado hacerlo pero se puede
lista_datos_separada = manejador.separar_palabras(lista_datos_original)

#Formato:
#   [
#       [
#           ["Las","cosas","felices","alegres","1"],
#           ["las","cosas","tristes","1"]
#       ],
#       [
#           ["Las","cosas","felices","2"],
#           ["las","cosas","tristes","2"]
#       ]
#   ]
lista_datos_normalizada = normalizar.normalizar_lista(lista_datos_separada)

#lista_datos_graficar = analizador.contar_palabras(lista_datos_normalizada)
#print()
graficador.generar_grafico2(lista_datos_normalizada)

lector.guardar_a_json(lista_datos_normalizada, lista_personalidades, "datos_normalizados.txt")
