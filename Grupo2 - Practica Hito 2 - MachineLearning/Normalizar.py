import re, string, unicodedata
import nltk
#import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

class normalizar:
    def remove_non_ascii(self,words):
    #   Remove non-ASCII characters from list of tokenized words
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    def to_lowercase(self,words):
    #Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words

    def remove_punctuation(self,words):
    #Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words

    def replace_numbers(self,words):
    #"""Replace all interger occurrences in list of tokenized words with textual representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words

    def remove_stopwords(self,words):
    #"""Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word in ['si','no']:
                new_words.append(word)
            if word not in stopwords.words('spanish'):
                new_words.append(word)
        return new_words

    def stem_words(self,words):
    #"""Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems

    def lemmatize_verbs(self,words):
    #"""Lemmatize verbs in list of tokenized words"""
    #esta ya saca en singular
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas    

    def normalize(self,words):
        words = self.remove_non_ascii(words)
        words = self.to_lowercase(words)
        words = self.remove_punctuation(words)
        words = self.replace_numbers(words)
        words = self.remove_stopwords(words)
        
        return words

    def normalizar_lista(self,lista_datos):
        lista_normalizada = []
        for respuesta_encuesta in lista_datos:
            nueva_respuesta_encuesta = []
            for respuesta_pregunta in respuesta_encuesta:
                nueva_respuesta_pregunta = self.normalize(respuesta_pregunta)
                nueva_respuesta_encuesta.append(nueva_respuesta_pregunta)
            lista_normalizada.append(nueva_respuesta_encuesta)
        return lista_normalizada