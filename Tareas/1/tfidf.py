from math import log
from collections import Counter
from functools import reduce

def bm25(x, k=25):
    return ((x + 1)*k)/(x+k)

def tf(documento, func=bm25):
    c = Counter(documento)
    return {
        termino : bm25(cuenta) for (termino, cuenta) in c.items()
    }

def idf(palabra, documentos):
    return log(
        len(documentos) / 
        (1+reduce(lambda cuenta, documento : cuenta + (1 if (palabra in documento) else 0), documentos, 0))
    )

def tfidf(tf : dict, idfs : dict):
    return {
            palabra: idfs[palabra]*tf_value
            for (palabra, tf_value) in tf.items()
    }

def obtener_keywords(tfidfs, num_keywords=5):
    keywords = []
    for tfidf_n in tfidfs:
        keywords_n = sorted(tfidf_n.items() ,  key=lambda x: x[1], reverse=True)[:num_keywords]
        keywords.append([keyword[0] for keyword in keywords_n])
    return keywords