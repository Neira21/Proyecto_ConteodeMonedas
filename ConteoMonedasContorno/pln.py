#### SPACY ####

# import spacy
# from spacy import displacy
# doc=pln("Esto es una frase de pruebas, para analizar texto.")

#pos_: indica si las palabras en la frase son pronombres, auxiliares, adjetivos, determinantes, etc.
# for palabra in doc:
#     print(palabra, palabra.pos_)
# doc2 = pln("Esta la primera frase. Esta la segunda frase. Esta la tercera frase.")

#.sents separa el documento en 
# for frase in doc2.sents:
#     print(frase)
# doc3 = pln("Los coches eléctricos será decisivos para afrontar las nuevas megatendencias de la sociedad del futuro")

# noun_chunks: Separar por componentes importantes que se considera dentro de la frase
# for parte in doc3.noun_chunks:
#     print(parte)
# doc4 = pln("Google ha comprado una empresa por 5 millones de euros")

# #displacy.render(doc4, style='dep', jupyter=False, options={"distance":100})

# El .serve crea un servidor indicando el style que puede ser 'dep' para 
# mostrar dependencias o 'ent' para identificar organizaciones

# displacy.serve(doc4, style='dep')
# doc4 = pln("KOI y Koi compradon una empresa por 5 millones de dólares")
# displacy.serve(doc4, style='ent', options={"distance":150})
# for palabra in doc4:
#     print(palabra, palabra.pos_)



#### STOP WORDS

# import spacy

# pln = spacy.load('es_core_news_sm')


#Muestra un diccionario con palabras que el sistema considera poco significativas
# print(pln.Defaults.stop_words)
# print(len(pln.Defaults.stop_words))

#Saber si una palabra se encuentra, True si es que está, False lo contrario
# print(pln.vocab['tb'].is_stop)

#Añadir palabra y luego cambiar de false a true, para agregar la nueva palabra
# pln.Defaults.stop_words.add('tb')
# pln.vocab['tb'].is_stop=True
# print(pln.vocab['tb'].is_stop)

#Para quitar un palabra
# pln.Defaults.stop_words.remove('tb')
# pln.vocab['tb'].is_stop=False




### MATCHER ###

import spacy
from spacy.matcher import Matcher

#Cargar el diccionario en español previamente instalado
pln = spacy.load('es_core_news_sm')

# Se crea una variable tipo matcher donde se le pasa como parámetro el 
# vocabulario del diccionario en español
matcher = Matcher(pln.vocab)

patron = [{'LOWER':'coche'}]






