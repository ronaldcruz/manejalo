manejalo
========

Sitio para ofrecer la venta y compra de vehículos.

## Instalación

###Backend

1. Clonar proyecto en tú workspace
2. Establecer un entorno a través de [virtualenv](http://www.virtualenv.org/en/latest/) para el proyecto.
3. Instalar los modulos necesarios para el proyecto con el ambiente activado.

```
$ cd $WORSPACE/manejalo/src/manejalo
$ pip install -r requirements.txt
```

Además se debe sincronizar la base de datos:

```
python manage.py syncdb
```

Finalmente correremos las migraciones

```
python manage.py migrate
```



###HayStack

[Haystack](http://haystacksearch.org/) es el módulo encargado de realizar las búsquedas en el sitio.

Primero debemos ingresar a la carpeta donde instalaremos Solr, la definiremos como $FOLDER_SOLR


```
$ curl -O https://archive.apache.org/dist/lucene/solr/3.5.0/apache-solr-3.5.0.tgz
$ tar xvzf apache-solr-3.5.0.tgz
$ cd apache-solr-3.5.0
$ cd example
$ java -jar start.jar
```

Luego, en el directorio del proyecto ejecutar:

```
python manage.py build_solr_schema > $FOLDER_SOLR/example/solr/conf/schema.xml
```

Esto generará el esquema de la base de datos que será indexada para las búsquedas. Posteriormente a esto indexamos el contenido.

```
python manage.py rebuild_index
```