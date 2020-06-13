# Análisis persuasivo en boletines de prensa en las elecciones de México 2018

## Universidad Nacional Autónoma de México

### Facultad de Ingeniería

#### Análisis y Procesamiento Inteligente de Textos

##### Semestre 2020-2

##### Equipo:

- Aguilar Enriquez, Paul Sebastian
- Alemán, Gustavo Adolfo
- Esparza, Luis Mauricio
- González Flores, Andrés

## Introducción

<!--
Hablar de cuál es el contenido del documento.

Esto lo puedo hacer al final (Paul).
-->

### Motivación

En la actualidad existen proyectos sobre Procesamiento de Lenguaje Natural (PLN)
que logran trabajar con grandes cantidades de datos de manera eficiente y con
resultados más que interesantes, sin embargo, muchos de estos se ejecutan desde
contextos completamente teóricos o con datos genéricos sin una aplicación que
resuelva un problema de manera directa.

En esta ocasión, quisimos buscar un problema en el cual se pudieran aplicar los
conocimientos de PLN y que sirvieran a una contribución mayor en un contexto
local.

Para lo anterior, era necesario que el problema en el que fuéramos a contribuir
requiriera procesar y analizar información como parte de su análisis y abordaje.

**El problema seleccionado fue el correspondiente al expuesto en el proyecto de 
tesis de la licencienda María Del Roció Flores Martínez, grado Maestría en 
Comunicación, el cual se titula "Uso y discurso del boletín de prensa en la 
comunicación política de los candidatos presidenciales en México (elecciones 
2018)".**

### Justificación

La tesis de la Lic. Flores plantea cómo objetivo general lo siguiente:

~~~
Analizar el discurso periodístico del boletín de prensa, así como el uso
persuasivo de este instrumento informativo, en la comunicación política de los
candidatos participantes en la elección presidencial del 1 de julio de 2018 en
México, con el fin de establecer su función como mediador en el sistema de
comunicación de masas.
~~~

Y tiene cómo pregunta eje:

~~~
¿Cuáles fueron el discurso periodístico y el uso persuasivo del boletín de
prensa en las estrategias comunicativas de los tres candidatos más votados en
las elecciones presidenciales de 2018 en México, durante la campaña
político-electoral de abril-junio?
~~~

Para lo anterior, la Lic. Flores en su tesis ha realizado una propuesta de
**análisis sobre los boletines de prensa en México**, en la cual busca
**categorizar el discurso periodístico y el persuasivo contenidos en los
boletines de prensa que emitieron los tres
candidatos presidenciales**.

El análisis propuesto toma a los boletines de prensa como un corpus a analizar
proponiendo diferentes elementos como categorías bien definidas e identificadas.
A su vez, los boletines de prensa son de acceso público por lo cual se pueden
descargar de la fuente original, contienen una estructura bien definida la cual
se puede analizar y, en conjunto, forman un grupo de datos consistente, que 
permite procesarlos de manera automatizada. El universo de estudio se compone
de 347 textos.


### Problema

La propuesta de análisis sobre los boletines de prensa surge de un estudio más 
profundo que lo aquí reflejado. Este se divide en dos niveles:

- **Nivel persuasivo:** (Primer nivel) busca evidenciar las técnicas persuasivas
de que se valieron los candidatos y la forma en como fueron reproducidos por sus
respectivos equipos de prensa en los boletines de prensa.
- **Nivel periodístico:** (Segundo nivel) éste se basará en examinar la
transgresión o cumplimiento del [Principio de Cooperación y las máximas de
Paul Grice](https://es.wikipedia.org/wiki/Paul_Grice#M%C3%A1ximas_conversacionales),
y observar el uso del discurso referido (directo e indirecto), mediante los
verbos de habla ([verba dicendi](https://en.wikipedia.org/wiki/Verbum_dicendi)).


#### Nivel persuasivo

En este nivel se proponen las siguientes categorías:

##### Categoría Cognitiva

1. **Construcción del emisor/candidato (C1):** el candidato se coloca como referente principal del acto discursivo para exaltar sus cualidades personales y erigirse, a los ojos de sus interlocutores, como un líder en quien es adecuado confiar para el desarrollo de acciones de gobierno a favor de la sociedad; esto lo lleva a cabo mediante realizaciones léxicas de la primera persona, en singular o plural, y formas flexivas de verbos y posesivos para referirse a sí mismo, ya sea como individuo o como miembro de una colectividad. Para el caso de la campaña presidencial que nos ocupa, las cualidades del candidato emitidas por un tercero en el marco de una tarea proselitista, quedarán incluidas en esta categoría, ya que contribuyen a construir la imagen positiva del contendiente.

2. **Promesa de campaña (C2):** a través de piezas discursivas, orales o escritas, el candidato oferta, destaca o compromete acciones que proyecta convertir en políticas públicas a favor de la población, si obtiene el triunfo en las urnas, con lo que implícitamente solicita el voto ciudadano que lo llevaría al poder.

##### Categoría Emocional

3. **Construcción del adversario (E1):** el mensaje es dirigido a su contraparte en la contienda electoral y está construido a manera de réplica y puede usar diferentes figuras retóricas (metáfora, ironía, metonimia) para conformar en el receptor una imagen determinada del adversario, que esencialmente tiene finalidad de descrédito.

4. **Exageración de la información (E2):** se destacan los datos favorables a los fines persuasivos, con el objetivo de crear una idea positiva en la mente del receptor referente al tema del que se habla, o incluso negativa respecto de información relativa al adversario; el persuasor desfigura el sentido original del acontecimiento, nos dice Roiz (1994), mediante códigos diferentes: humorístico, burlesco, cínico, entre otros.

5. **Recurso retórico (E3):** son variables basadas en figuras retóricas (metáfora, ironía, hipérbole, personificación, pleonasmo, perífrasis) que pueden fortalecer el efecto persuasivo, de acuerdo con Reardon (1991).

6. **Apelación al miedo (E4):** el candidato emite mensajes dentro de su alocución que pretenden provocar sentimientos de aprensión, desasosiego o preocupación con respecto al adversario o a sus propuestas. 

##### Categoría Volitiva

7. **Llamado al voto (V1):** el emisor del mensaje hace una invitación directa al ciudadano para que apoye su proyecto político el día de la elección al depositar el sufragio a su favor.


#### Nivel persuasivo

En este nivel se proponen los siguientes elementos:

- **Máxima infringida:**
  - **Máxima de calidad:** Omite información falsa o de la que no tenga
  constancia o conocimiento suficiente.
  - **Máxima de cantidad:** Ofrece la información necesaria, ni más ni menos, de
  acuerdo con la conversación en la que esté inmerso.
  - **Máxima de modo:** Habla (o escribe) con claridad, evitando ambigüedades
  que hagan “ruido” en la conversación. Se refiere al modo en que se comunican
  los participantes.
  - **Máxima de relación (o pertinencia):** Hace que su contribución en la
  conversación sea pertinente.
- **Tipología Discurso Referido (DR) indirecto:**
  - **Descripción:**. Es para señalar las características de un objeto. Este
  tipo de descripción tiene cabida en géneros periodísticos que interpretan la
  realidad; por ejemplo, la crónica y el reportaje.
  - **Narración:** Propone relatar un suceso o serie de sucesos relacionados, de
  tal manera que adquieren un significado distinto de aquel que tienen por
  separado. Para narrar es preciso seleccionar aquellos datos que mejor
  caracteriza la imagen que se desea transmitir y, además, incluir personajes
  que realicen acciones. Por ejemplo la crónica y el reportaje.
  - **Exposición:** Enuncia los hechos y las ideas. Su propósito es explicar la
  naturaleza de un objeto, una idea o un tema. Se refiere a los pensamientos,
  por ello de las cuatro formas discursivas es la que se dirige más al intelecto
  que a las emociones. Es común encontrarla junto a la argumentación. En el
  periodismo, esta forma discursiva es utilizada en la nota informativa.
  - **Argumentación:** Su propósito central es convencer al lector para que
  adopte determinada doctrina o actitud. Por su interés persuasivo, la
  argumentación se dirige al intelecto y a los sentimientos de las personas. Se
  basa más en la lógica natural de la vida cotidiana que en la lógica formal del
  razonamiento demostrativo. Los artículos de opinión son el espacio
  periodístico en el que se manifiestan los argumentos.
- **Verba dicendi:**

| NÚM\. | TIPO | VERBOS | CLAVE |
|-|-|-|-|
| 1 | De opinión | opinar, considerar, juzgar, reputar, apoyar, creer, desaprobar | V1 |
| 2 | De valoración positiva | alabar, aclamar, halagar, aplaudir, aprobar, celebrar, felicitar, elogiar, aclamar, bendecir, piropear, vitorear | V2 |
| 3 | Verbos de valoración negativa | acusar, criticar, reprochar, rechazar, corregir, calumniar, castigar, maldecir, censurar, reprender, culpar, denunciar, descalificar, ridiculizar, responsabilizar, alertar | V3 |
| 4 | Verbos declarativos | aclarar, decir, comunicar, mencionar, notificar, responder, manifestar, contestar, declarar, mantener, observar, sostener, señalar, pronunciar, transmitir, opinar, expresar, comunicar, aconsejar, apuntar, avisar, comentar, considerar, escribir, indicar, informar, insinuar, notificar, proponer, recomendar, sugerir | V4 |
| 5 | Verbos de manera de decir \(o fuerza de expresión: López Quero, 2019\) | arremeter, cuestionar, debatir, destacar, resaltar, preguntar, gemir, gritar, susurrar, chillar, balbucear, balbucir, cotillear, cotorrear, deletrear, mascullar, bisbisear, canturrear, chacharear, salmodiar, parlotear, tartamudear, cuchichear, silabear, proclamar, proferir, murmurar, declamar, prorrumpir, comadrear, chismorrear, enfatizar | V5 |
| 6 | Verbos de orden o mandato | mandar, ordenar, encargar, prohibir, arengar | V6 |
| 7 | Verbos de petición o ruego (también llamados de orden o “de voluntad”: Reyes, 1995\) | rogar, pedir, suplicar, exigir, demandar, solicitar, exclamar, sugerir, ordenar, clamar, exhortar | V7 |
| 8 | Verbos declarativos con valor prospectivo | anunciar, pronosticar, augurar, prometer, jurar, avisar, advertir, amenazar, rezar, orar, profetizar, pronosticar, adelantar, vaticinar, prever | V8 |
| 9 | Verbos que indican la verdad o la falsedad del discurso citado | revelar, pretender, aseverar, afirmar, negar, aclarar, confirmar, contradecir, asegurar, corroborar, asentir, demostrar, disentir, mentir, sentenciar, testimoniar, rectificar, desmentir | V9 |
| 10 | Verbos que sitúan el discurso citado en la orientación argumentativa | repetir, concluir, responder, alegar, ampliar, convenir, atestiguar, defender, diferir, definir, contestar, argüir, argumentar, describir, detallar, diferenciar, citar, discutir, refutar, retrucar, oponer, valorar, rebatir, parlamentar, ponderar, perorar, parafrasear, puntualizar, objetar, explicar, exponer | V10 |
| 11 | Verbos que inscriben el discurso citado en una de las distintas formas de narrar | relatar, contar, confesar, reseñar, comentar, referir, resumir, sintetizar, nombrar, abreviar | V11   |
| 12 | Verbos que expresan sentimiento | lamentar, arrepentirse, sorprender, alegrarse, asombrarse, entristecerse, amargarse, admirarse, rezongar, ofender, vanagloriarse, protestar, disculparse, confiar, desconfiar, temer | V12   |
| 13 | Verbos que se refieren a modos de conversar | conferenciar, conversar, dialogar, charlar, discursear, sermonear, predicar, saludar, suavizar, subrayar, platicar | V13   |
| 14 | Verbos que se refieren a procesos intelectuales | pensar, recordar, reflexionar, meditar, enumerar, razonar, relacionar | V14   |
| 15 | Verbos que se refieren a la poesía | versificar, recitar, cantar, tararear | V15   |
| 16 | Verbos compromisorios | asegurar, comprometerse garantizar, prometer, asumir | V16 |
| 17 | Verbos de citación | emplazar, retar | V17   |
| 18 | Verbos de petición manifiesta | Llamar, pedir, reclamar, solicitar | V18   |
| 19 | Verbos de petición implícita | invitar, ofrecer, plantear \(REVISAR ¿\), proponer, sugerir | V19 |
| 20 | Verbos con valor retrospectivo | admitir, confirmar, defender, insistir, justificar, negar, negarse, ratificar, reafirmar, rechazar, reconocer, recordar, rectificar, reiterar, replicar, revelar, sostener, refrendar | V20 |


Debido a los elementos del análisis propuesto por la Lic. Flores y a la cantidad
de boletines de prensa emitidos convendría automatizar esta tarea por dos
razones:

- Si bien la cantidad de boletines no es demasiado extensa (347), para una sola
persona trabajar sobre tantos documentos puede no ser viable.
- Verificar si los elementos propuestos como parte del análisis de los boletines
de prensa se pueden obtener mediante herramientas de PLN o de Aprendizaje
Maquina (Machine Learning, ML).

### Solución propuesta

<!-- Verificar con el equipo -->
Como propuesta inicial (y por tiempo) se ha optado por trabajar solamente con el
análisis del nivel persuasivo y sus categorías propuestas.

#### Latent Dirichlet Allocation (LDA)

El primer método que se plateó para ser utilizado en la resolución del problema, 
nos planteamos utilizar LDA para generar un modelo estadístico que nos permitiera
analizar y agrupar los grupos formados y definidos por la Licenciada Flores.

Partiendo de datos obtenidos y de palabras previamente clasificadas, habríamos
sido capaces de analizar la pertenencia de un conjunto no obseravdo de palabras 
con respecto a las categorías cognitivas específicadas en nuestro problema.

Suponiendo que cada documento esta compuesto por un conjunto de palabras,
mismas que tienen una alta probabilidad de pertenecer a uno o dos tópicos, podemos
estimar la pertenencia de aquellas palabras desconocidas a alguno de ellos. Con lo
anterior sería posible generar un modelo que fuera capaz tanto de generar documentos
para cada tópico, como de ayudarnos a estimar la pertenencia de un documento nuevo
con respecto al modelo entrenado.

Haciendo clustering de las palabras similares lograríamos confirmar y clasificar de 
manera veloz a todos aquellos documentos que no han sido observados previamente.
Cada palabra recibe una pertenencia a uno o más tópicos basándose en la pertenencia
a dichos tópicos de las palabras con las que comparta el documento.

Este procedimiento también nos ayuda con la limpieza de las palabras poco relevantes,
i.e., aquellas tan comunes que resulta imposible asignarlas a un tópico; permitiéndonos
calcular la probabilidad de que una palabra importante defina tanto el tópico al que 
pertence un documento, como la probabilidad de que ocurran instancias pertenecientes
al mismo tópico dentro del mismo.

<!--
A través de algoritmos de clusterización y embedings encontrar las categorías
que pudieran existir en los tópicos de los boletines y su representación
vectorial para ver cómo se correlacionan.

Igual que los dos puntos anteriores. (Paul y Andrés)
-->

## Marco Teórico-Metodológico

### Antecedentes

<!--
¿Qué se ha hecho antes?
-->
#### Análisis de Sentimientos utilizando LSTM

Las LSTM han sido ámplimente utilizadas para hacer análisis de casi cualquier tipo 
de datos, entre ellos está el análisis de video, voz, pero la principal aplicación es
el análisis de textos.

Con el análisis de sentimientos se pretende identificar y categorizar opiniones basadas
únicamente en el texto presente en ellas, con el propósito de determinar la postura, sea
positiva o negativa, del autor frente a un tópico, objeto, persona, etcétera.

El análisis se puede segmentar en:
* Tokenización de las palabras
* Capa de Embeding
* Capa LSTM
* Capa de Conexión
* Capa de Activación
* Salida

Se resume al proceso de limpiado de datos, representación de éstos dentro de un espacio 
vectorial para mayor facilidad en su categorización, el uso de la LSTM para aprender 
información y retenerla por un largo plazo sin necesidad de entrar en problemas de 
dependencia a largo plazo, i.e., cuando la información presente depende de información 
pasada, pero muy distante. La capa de conexión se encarga de relacionar las salidas de
las LSTM a un tamaño deseado, de donde activamos cada salida y entregamos un resultado
final.

En el análisis de sentimientos, las LSTM nos ayudan a predecir la intención de un mensaje
haciendo de las categorías de las palabras así como relacionándolas con las palabras que
ha visto anteriormente, de modo que no resulta arriesgado implementar un modelo similar
para encontrar la correspondencia con una categoría definida por alguien externo para
entontrar la pertenencia de un documento a alguna de ellas, en lugar de encontrar el
sentimiento que expresan.


### Trabajos relacionados

El análisis político es un tema que ha sido reservado casi exclusivamente para carreras
de otras áreas, muchas veces haciendo énfasis en la construcción paulatina de un estudio
a lo largo de los años y con el esfuerzo de varios académicos.

Es raro encontrar que, en México, la tecnología sea aplicada a los intereses de análisis
político, por lo que el proyecto elaborado no cuenta con una base sobre la cuál soportarse
que no sea un trabajo académico, o, en éste caso, una tésis de grado.

La información encontrada ha sido exclusiva a dos áreas: la gramatical y académica, 
perteneciente al área política; y la tecnológica y técnica, perteneciente al desarrollo
y aplicación de redes neuronales recurrentes.

Como parte del desarrollo de éste proyecto va orientado a proveer un apoyo al análisis
necesario y veloz para una tésis, no es posible compartir la totalidad de ésta, que sigue
en proceso de elaboración. Sin embargo, todo lo necesario ya ha sido mencionado y agregado
en las primeras partes de éste reporte.
<!--
¿Dónde lo han aplicado o dónde podemos encontrarlo?
-->

### Descripción

<!--
De la teoría a utilizar

Aquí, mencionar a detalle las herramientas que usaremos:

- De donde sacamos los corpus
- Mongo y Compas
- Clusterización
- Embedding
-->
El proyecto requirió de obtener primeramente los boletines de prensa, éstos los tomamos
directamente de las páginas de los candidatos. Para cada uno se recuperaron de sus
propias páginas web, de las que se tuvo que realizar un scrapping.

Las siguientes herramientas que fueron utilizadas para la elaboración del proyecto fueron:

#### MongoDB y Compass

Para el almacenamiento de la información procesada, se utilizó MongoDB, y especialmente,
su herramienta Compass para visualizar la información de manera gráfica, ya que Compass
integra una herramienta capaz de realizar el análisis del esquema utilizado, de modo que
se pudo visualizar información útil acerca de nuestro dataset.

#### Clusterización
<!-- Aquí tenemos que exponer la herramienta o método utilizado para la clusterización -->

## Método Experimental

### Datos

#### Descripción del set de datos

Los boletines de prensa con los que se trabajo corresponden a tres momentos:

- Inicio de campaña.
- Primer debate.
- Segundo debate.

El set de datos cuenta con 344 boletines de prensa los cuales se obtuvieron de
sus fuentes oficiales:

- Enlace a los boletines
- Enlace a los boletines
- Enlace a los boletines

Para el candidato Andrés Manuel López Obrador de emitieron 83 boletines de
prensa.

Para el candidato Ricardo Anaya Cortés se emitieron 114 boletines de prensa.

Y para el candidato José Antonio Meade Kuribreña se emitieron 147 boletines de
prensa.

Los documentos en general cuentan con la siguiente estructura:

- Encabezado
- Sumario o Balazos
- _Lead_ o Primer Párrafo
- Cuerpo

#### Obtención de los datos

Para la obtención del set de datos se recurrió a dos medios:

- Solicitudes de transparencia
- Acceso a fuentes publicas (referidas en las respuestas a las solicitudes de
  transparencia)

##### Candidato AMLO

- [Respuesta a solicitud de transparencia](./Corpus/AMLO/Respuesta2230000052819.md).
- Boletines
  - En formato doc, [aquí](./Corpus/AMLO/docs).
  - En texto plano, [aquí](./Corpus/AMLO/txt).
  - En web: [http://lopezobrador.org.mx/](http://lopezobrador.org.mx/)

##### Candidato JAMK

- [Respuesta a solicitud de transparencia](./Corpus/JAMK/RespTransparencia2237000009019_030519.md).
- Boletines
  - En formato doc, [aquí](./Corpus/JAMK/docs).
  - En texto plano, [aquí](./Corpus/JAMK/txt).
  - En web: [http://pri.org.mx/SomosPRI/saladeprensa/Categorias.aspx?y=3](http://pri.org.mx/SomosPRI/saladeprensa/Categorias.aspx?y=3).
- Boletines que no están como docx
  - [http://pri.org.mx/SomosPRI/SaladePrensa/Nota.aspx?y=30565](http://pri.org.mx/SomosPRI/SaladePrensa/Nota.aspx?y=30565)
  - [http://pri.org.mx/SomosPRI/SaladePrensa/Nota.aspx?y=30455](http://pri.org.mx/SomosPRI/SaladePrensa/Nota.aspx?y=30455)

##### Candidato RAC

- [Respuesta a solicitud de transparencia](./Corpus/RAC/Respuesta-73-19.md).
- Boletines
  - En formato doc, [aquí](./Corpus/RAC/docs).
  - En texto plano, [aquí](./Corpus/RAC/txt).
  - En web: la cuenta [ricardoanaya.com.mx](ricardoanaya.com.mx) fue cerrada el 26 de marzo de 2019.
  - ![Screenshot página suspendida](./Corpus/RAC/ss-pag-suspendida.png)

<!-- Hay algun metodo de scraping? -->

#### Limpieza de los datos

<!-- Revisas que onda con MongoDB y Compas -->
No es posible trabajar con los datos sin realizar la limpieza de las palabras, de modo que sólo
conservaremos las palabras relevantes en los formatos que busquemos y consideremos útiles.
Para ésto, después del web scrapping, la limpieza de elementos no léxicos y correcciones de
formato para encabezados, sumarios y boletines en general (doble espacio, salto de línea, 
acentos, etcétera). Para ésto, la tarea se segmentó en varios pasos:

##### Preprocesamiento de Encabezados y Sumarios
Se limpian los espacios y caracteres no léxicos (innecesarios) de los boletines en la BD.

##### Preprocesamiento de Boletines
Se cambia el nombre de los archivos para que tengan el mismo formato. Además, se modifico 
el contenido de los boletines, quitando espacios dobles y más caracteres especiales, entre
otros casos especiales en un par de boletines.

##### Emparejamiento de cada Encabezado con su Boletín
Se emparejan los encabezados con el texto correspondiente a su boletín dentro de la BD. El
formato final es internamente almacenado en csv.

##### Emparejamiento de Metadatos con su Boletín
Se hace la búsque acera de los identificadores utilizados por los equipos de prensa para enumerar
sus boletines/comunicados. Ésto es guardado en la BD.

##### Limpieza de Encabezados y Sumarios para cada Boletín.
Se elimina la información del contenido principal del archivo de la base de datos. Éstos ya se
encuentran estructurados dentro de cada archivo, por lo que es innecesario retenerlos.

#### Encoding / Tokenización de los datos

<!-- Revisas que onda con MongoDB y Compas -->

### Descripción de su método

<!--
Aquí, hablamos de nuestra teoria propuesta

- Clusterización
  - Latent Dirichlet Allocation
- Embedding
-->
#### Clusterización

#### LSTM en lugar de LDA

Inicialmente habíamos considerado utilizar LDA, sin embargo, nos pareció más útil recurrir
a un LSTM, que nos proporcionó más utilidad para el problema a resolver. LDA no fue del todo
inútil, pero su implementación no llegó a culminarse antes de decidir un cambio.
Comparado con un LSTM, ambos nos permiten etiquetar y clasificar, pero LDA se encontraba
más orientado a la generación de documentos basádo en palabras y tópicos, mientras que LSTM,
mientras realiza algo similar, nos permite estar retroalimentándonos de estados anteriores
dentro de nuestros mismos documentos, por lo que, finalmente, fue la herramienta que utilizamos.

#### Embedding

De modo que, realizar embedding de palabras nos proporciona una representación mucho más profunda
acerca de cada una de ellas, decidimos utilizar ésta técnica por sobre la bolsa de palabras para
poder hacer clasificaciones más correctas.
Cada palabra quedaría dispuesta en un espacio vectorial donde cada vector representaría la pertenencia
de cada una de nuestras palabras con respecto a las categorías determinadas. La posición de cada uno
de nuestros vectores sería determinada y entrenada utilizando nuestro dataset de boletines políticos.


### Descripción del experimento

<!--
Aquí, cómo lo hicimos
-->

### Presentación de resultados

<!--
Aquí, mostramos resultados wuiiiiiiiiiiiiiiiiiii
-->

## Conclusión

<!--
Todo esto hasta el final :'v
-->

### Discusión de sus resultados

### Descripción de observaciones

### Trabajo futuro
