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

- **Categoría Cognitiva:**
  - **C1:** Construcción del emisor/candidato.
- **Categoría Emocional:**
  - **E2**: Construcción del adversario.
  - **E3:** Exageración de la información.
  - **E5:** Recurso metafórico.
  - **E6:** Apelación al miedo.
- **Categoría Volitiva:**
  - **V7:** Llamado al voto.

#### Nivel persuasivo

En este nivel se proponen los siguientes elementos:

- **Máxima infringida:**
  - **Máxima de calidad:** Ofrece la información necesaria, ni más ni menos, de
  acuerdo con la conversación en la que esté inmerso.
  - **Máxima de cantidad:** Omite información falsa o de la que no tenga
  constancia o conocimiento suficiente.
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

<!--
A través de algoritmos de clusterización y embedings encontrar las categorías
que pudieran existir en los tópicos de los boletines y su representación
vectorial para ver cómo se correlacionan.

Mencionar sobre Latent Dirichlet Allocation (Mau)

Igual que los dos puntos anteriores. (Paul y Andrés)
-->

## Marco Teórico-Metodológico

### Antecedentes

<!--
¿Qué se ha hecho antes?
-->

### Trabajos relacionados

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
  - Latent Dirichlet Allocation
- Embedding
-->

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

#### Encoding / Tokenización de los datos

<!-- Revisas que onda con MongoDB y Compas -->

### Descripción de su método

<!--
Aquí, hablamos de nuestra teoria propuesta

- Clusterización
  - Latent Dirichlet Allocation
- Embedding
-->

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
