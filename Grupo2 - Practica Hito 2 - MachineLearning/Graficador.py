import numpy as np
import matplotlib.pyplot as plt

class Graficador:
    
    def generar_grafico_personalidades(self, lista_datos_final):
        
        ticks = lista_datos_final[0]
        valores = lista_datos_final[1]
        N = len(ticks)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence

        plt.bar(ind, valores, width)
        

        plt.ylabel('Scores')
        plt.title('Scores by group and gender')
        plt.xticks(ind, ticks)
        plt.yticks(np.arange(0, 81, 10))

        plt.show()
       
    def generar_grafico2(self, lista_datos):
        import nltk
        from nltk import FreqDist 
        lista_unica=""   
        for respuesta_encuesta in lista_datos:
            for respuesta_pregunta in respuesta_encuesta:
                for palabra in respuesta_pregunta:
                    lista_unica+=palabra + " "
        tokens = nltk.word_tokenize(lista_unica)
        fdist=FreqDist(tokens)
        print(fdist.keys())
        print(fdist.values()) 
        fdist.plot(30, cumulative=False)  