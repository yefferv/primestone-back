# _CRUDs Clientes - Sockets - Medidores 


## Descripcion del problema 🚀

_Se debe crear una API REST para la creacion,lectura, modificacion y eliminacion de las entidades de clientes ,_ 
_sockets(puntos de media) y medidores teniendo en encuenta que un cliente puede tener varios puntos de medida asociados,_
_y un punto de media puede tener varios medidores. La informacion se almancenara en base de datos Postgres. 



### Descripción de la configuración del entorno de trabajo 🔧

_El IDE utilizado : _
```
Visual Studio Code
```

_librerias utilizadas : _

```
virtualenv==20.0.26
Python==3.8.3
Flask==1.1.2
flask-marshmallow==0.13.0
Flask-SQLAlchemy==2.4.4
psycopg2==2.8.5
```

_Sistema Operativo : _
```
Windows 10 enterprise
```

## resolver el problema. 
_Tendiendo las entidades planteadas en el problema (clientes, socker, medidores) con su respectiva realacion , lo primero que hice fue _
_definir los atributos qeu se van a manejar para cada entidad, una vez teniendo el modelo escrito, definir la estructura de carpetas._
_la idea es tener todo separado, como lo es el modelo (con cada entidad) , las rutas (un archivo de rutas para cada entidad )  y el_ _archivo principal (app.py) en el cual se pone a correr la aplicación._


* **Yeffer Velandia** 
