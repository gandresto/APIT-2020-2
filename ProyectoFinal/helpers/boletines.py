from pymongo import MongoClient
# from pprint import pprint

pipeline_sentences_freeling = [
    {
        '$project': {
            'sentences': {
                '$concatArrays': [
                    {
                        '$map': {
                            'input': '$encabezado', 
                            'as': 'sent', 
                            'in': '$$sent.token'
                        }
                    }, {
                        '$map': {
                            'input': '$sumarios', 
                            'as': 'sent', 
                            'in': '$$sent.token'
                        }
                    }, {
                        '$map': {
                            'input': '$boletin', 
                            'as': 'sent', 
                            'in': '$$sent.token'
                        }
                    }
                ]
            }
        }
    }, {
        '$unwind': { 'path': '$sentences' }
    }, {
        '$addFields': { 'sent_len': { '$size': '$sentences' } }
    }, {
        '$match': { 'sent_len': { '$gte': 5 } }
    }, {
        '$group': {
            '_id': None, 
            'sentences': { '$push': '$sentences' }, 
            'count': { '$sum': 1 }, 
            'avg': { '$avg': '$sent_len' }, 
            'std': { '$stdDevSamp': '$sent_len' }, 
            'max': { '$max': '$sent_len' }, 
            'min': { '$min': '$sent_len' }
        }
    }, {
        '$limit': 1
    }
]

pipeline_sentences_corenlp = [
    {
        '$project': {
            'sentences': {
                '$concatArrays': [
                    '$boletin.tokens', '$encabezado.tokens', '$sumarios.tokens'
                ]
            }
        }
    }, {
        '$project': {
            'sentences': {
                '$map': {
                    'input': '$sentences', 
                    'as': 'sent', 
                    'in': {
                        '$map': {
                            'input': '$$sent', 
                            'as': 'token', 
                            'in': {
                                '$arrayElemAt': [
                                    '$$token', 0
                                ]
                            }
                        }
                    }
                }
            }
        }
    }, {
        '$unwind': {
            'path': '$sentences'
        }
    }, {
        '$addFields': {
            'num_tokens': {
                '$size': '$sentences'
            }
        }
    }, {
        '$project': {
            'sentence': {
                '$map': {
                    'input': '$sentences', 
                    'as': 'token', 
                    'in': '$$token.text'
                }
            }, 
            'num_tokens': 1
        }
    }, {
        '$match': {
            '$or': [
                {
                    'num_tokens': {
                        '$gt': 5
                    }
                }, {
                    '$and': [
                        {
                            'sentence': {
                                '$nin': [
                                    'Agenda', 'AGENDA', 'agenda'
                                ]
                            }
                        }, {
                            'num_tokens': {
                                '$lte': 5, 
                                '$gt': 2
                            }
                        }
                    ]
                }
            ]
        }
    }, {
        '$group': {
            '_id': None, 
            'sentences': {
                '$push': '$sentence'
            }, 
            'count': {
                '$sum': 1
            }, 
            'min': {
                '$min': '$num_tokens'
            }, 
            'max': {
                '$max': '$num_tokens'
            }, 
            'avg': {
                '$avg': '$num_tokens'
            }, 
            'std': {
                '$stdDevSamp': '$num_tokens'
            }
        }
    }
]

def sentences(mongo_uri: str, source='freeling'):
    """
    Devuelve un diccionario con todas las sentencias en encabezados, 
    sumarios y contenido de todos los boletines en el corpus. También,
    devuelve estadísticas de promedio, máximo, mínimo y desviación estándar.

    {
        'sentences' : <lista con todas las sentencias>,
        'min': <tamaño mínimo de sentencias en número de tokens>,
        'max': <tamaño máximo de sentencias en número de tokens>,
        'avg': <tamaño promedio de sentencias en número de tokens>,
        'std': <desviación estándar de sentencias en número de tokens>,
    } 

    :param mongo_uri: La url de conexión a MongoDB
    :param source: El destino de los enunciados. Pueden se de 'corenlp'
    o de 'freeling'
    :returns: Un diccionario con oraciones por candidato.
    """
    with MongoClient(mongo_uri) as client:
        if not client:
            raise ConnectionError
        
        if source=='freeling':    
            stats_freeling = client['boletines_db']['stats_freeling']
            result = stats_freeling.aggregate(pipeline_sentences_freeling)
        elif source=='corenlp':
            stats_freeling = client['boletines_db']['stats_corenlp']
            result = stats_freeling.aggregate(pipeline_sentences_corenlp)

        for doc in result:
            return doc 


def sentences_candidato(mongo_uri: str):
    """
    Devuelve un diccionario con todas las sentencias en encabezados, 
    sumarios y contenido de todos los boletines en el corpus.
    Las sentencias son agrupadas por candidato    

    :param mongo_uri: La url de conexión a MongoDB
    :returns: Un diccionario con oraciones por candidato.
    """
    with MongoClient(mongo_uri) as client:
        if not client:
            raise ConnectionError
        # print(client)
        db = client.boletines_db

        pipeline = []

        project_stage = { "$project": { '_id': 1, 'candidato': 1 } }
        pipeline.append(project_stage)

        lookup_stage = {
            '$lookup': {
                'from': 'stats_freeling', 
                'localField': '_id', 
                'foreignField': 'boletin_id', 
                'as': 'stats'
            }
        }
        pipeline.append(lookup_stage)

        unwind_stage = { '$unwind': { 'path': '$stats' } }
        pipeline.append(unwind_stage)

        # Recuperar solo token de cada sentencia
        sent_tokens = [
            {
                '$cond': [
                    {'$isArray': f'$stats.{campo}'},
                    { '$map': { 
                        'input': f'$stats.{campo}', 
                        'as': 'sent', 
                        'in': '$$sent.token'
                    }},
                    []
                ]
            }
            for campo in ['encabezado', 'sumarios', 'boletin']
        ]

        project_stage = {
            "$project": {
                '_id': 0,
                'candidato':1,
                'sentences': { # Solo nos interesan las sentencias
                    "$concatArrays": sent_tokens
                }
            }
        }
        pipeline.append(project_stage)

        group_stage = {
            '$group': {
                '_id': '$candidato',
                'sentences': {
                    '$push': '$sentences'
                }
            }
        }
        pipeline.append(group_stage)

        project_stage = {
            '$project': {
                '_id': 0,
                'candidato': '$_id',
                'sentences': {
                    '$reduce': {
                    'input': '$sentences',
                    'initialValue': [],
                    'in':{
                        '$concatArrays': [
                            '$$value',
                            '$$this'
                        ]
                    }
                    }
                }
            }

        }
        pipeline.append(project_stage)

        # print('Procesando pipeline...')
        # pprint(pipeline)
        cursor = db.boletines.aggregate(pipeline)

        freq_tokens = {}
        sentences = {}

        for doc in cursor:
            candidato = doc['candidato']
            print(candidato)
            sents = []
            for i, sentence in enumerate(doc['sentences']):
                if sentence is None:
                    break
                sents.append(sentence)
                if i%376 == 0:
                    print(f'{i+1}. {" ".join(sentence)}')
            sentences[candidato] = sents
            print()

    return sentences
