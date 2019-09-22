class Analizador_de_Datos:
    def palabras_op_pe(self,lista_datos_original,lista_personalidades):
        lista_optimista=[]
        lista_pesimista=[]

        for respuesta_encuesta in lista_datos_original:
            i = lista_datos_original.index(respuesta_encuesta)
            if (lista_personalidades[i] == "Optimista"):
                lista_optimista.append(respuesta_encuesta)
            else:
                lista_pesimista.append(respuesta_encuesta)
        
        return [lista_optimista,lista_pesimista]
        

    def contar_palabras(self,lista_datos):
        import nltk
        lista_unica = []
        for respuesta_encuesta in lista_datos:
            for respuesta_pregunta in respuesta_encuesta:
                for palabra in respuesta_pregunta:
                    lista_unica.append(palabra)
        
        lista_de_palabras = []
        lista_de_palabras_contadores = []
        for palabra in lista_unica:
            if palabra not in lista_de_palabras:
                lista_de_palabras.append(palabra)
                lista_de_palabras_contadores.append(1)
            else:
                indice = lista_de_palabras.index(palabra)
                lista_de_palabras_contadores[indice] += 1
        lista_final=[lista_de_palabras,lista_de_palabras_contadores]
        return lista_final

    lista_palabras_optimistas = ["si","solucion","mejor","suerte","busco","mas","sigo","seguir","intentando","vida"]
    lista_palabras_pesimistas = ["no","mal","mala","expectativas","siguiente","intentar","triste","trato"]

    def generar_resultados(self, lista_datos_normalizada, lista_palabras_optimistas, lista_palabras_pesimistas):
        lista_personalidades = []
        for respuesta_encuesta in lista_datos_normalizada:
            contador_optimista = 0
            contador_pesimista = 0
            for respuesta_pregunta in respuesta_encuesta:
                for palabra in respuesta_pregunta:
                    if palabra in lista_palabras_optimistas:
                        contador_optimista += 1
                    if palabra in lista_palabras_pesimistas:
                        contador_pesimista += 1
            
            if (contador_optimista >= contador_pesimista):
                lista_personalidades.append("Optimista")
            else:
                lista_personalidades.append("Pesimista")

        return lista_personalidades
