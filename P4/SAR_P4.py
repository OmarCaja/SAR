'''
Jose Antonio Culla de Moya
Omar Caja Garcia
'''

from nltk.probability import *

'''
Ejercicio 1 apartado 1
'''
from nltk.corpus import cess_esp

'''
Ejercicio 1 apartado 2
'''
print(len(cess_esp.words()))

'''
Ejercicio 1 apartado 3
'''
print(len(cess_esp.sents()))

'''
Ejercicio 1 apartado 4
'''
text = cess_esp.words(cess_esp.fileids()[0])
frecFile1 = FreqDist(text)
print(frecFile1.most_common(20))