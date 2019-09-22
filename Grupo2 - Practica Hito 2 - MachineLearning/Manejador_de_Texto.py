import nltk
#from nltk.tokenize import sent_tokenize

class Manejador_de_Texto:
    def separar_palabras(self, lista_datos_original):
        nueva_lista_datos = []
        for respuesta_encuesta in lista_datos_original:
            nueva_respuesta_encuesta = []
            for respuesta_pregunta in respuesta_encuesta:
                nueva_respuesta_pregunta = nltk.word_tokenize(respuesta_pregunta)
                # nueva_respuesta_pregunta = sent_tokenize(mytext,"spanish")
                nueva_respuesta_encuesta.append(nueva_respuesta_pregunta)
            nueva_lista_datos.append(nueva_respuesta_encuesta)
        return nueva_lista_datos


    #En lugar de usar todo esto usamos la clase Normalizar
    def omitir_palabras(self, lista_datos_separada):
        
        return True

    def unir_palabras(self, lista_datos_limpia):
        return True

    def plural_a_singular(self, lista_datos_limpia):
        for respuesta_encuesta in lista_datos_limpia:
            for respuesta_pregunta in respuesta_encuesta:
                for palabra in respuesta_pregunta:
                    print(palabra) #para que no de error por el momento
                    
