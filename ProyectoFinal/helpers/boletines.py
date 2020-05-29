from pymongo import MongoClient
# from pprint import pprint

def get_sentences(mongo_uri : str, ):
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
