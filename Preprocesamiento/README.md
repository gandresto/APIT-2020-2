# Preprocesamiento

## 1. Preprocesado Encabezados

Elimino espacios y caracteres innecesarios en los encabezados de la base de datos.

Jupyter notebook [aquí](./1_preprocesado_encabezados.ipynb).

## 2. Preprocesar Boletines

Cambio nombres de archivos para que tengan el mismo formato. Admás, modifico el contenido de los boletines, quitando espacios dobles, caracteres especiales y otros extras.

Jupyter notebook [aquí](./2_preprocesar_boletines.ipynb).

## 3. Emparejar contenido de boletines

Emparejo los archivos de texto con su correspondiente boletín en la base de datos. Guardo los resultados en archivos csv y en la base de datos.

Jupyter notebook [aquí](./3_emparejar_contenido_boletines.ipynb).

## 4. Emparejar metadatos

Busco información acerca del identificador que usaron los equipos de prensa originalmente para enumerar sus boletines o comunicados. Luego, los guardo en la base de datos.

Jupyter notebook [aquí](./4_emparejar_metadatos.ipynb).

## 5. Eliminar encabezado y sumarios

Elimino esta información del contenido principal del archivo en la base de datos, debido a que estos datos ya están estructurados dentro de ella.

Jupyter notebook [aquí](./5_eliminar_encabezado_sumarios.ipynb).
