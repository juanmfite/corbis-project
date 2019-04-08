
# Control de Stock para Test CorbisStudio

Este es un proyecto hecho en Django en el que se resuelve la consigna del test técnico.

### Especificaciones 📋

- Django 2.2
- Postgres 11.2
- Bootstrap
- Django Rest Framework
- Docker (docker-compose)

### Pre-requisitos

Se debe tener instalado docker y docker-compose. 

Tener libre el puerto 8000. 

### Despliegue 🔧

Se utilizó un contenedor Docker para dicho proyecto. El mismo esta hecho con un _docker-compose_.

Para desplegar el proyecto simplemente se debe ejecutar el script _init.sh_, el mismo contiene todos los comandos de docker junto con importanción de la base de datos.


_Explicación del funcionamiento del docker-compose_

En el docker-compose se crearon dos servicios, uno para la web y otro la base de datos. 

Para el servicio de la base de datos no se creo un volumen ya que se hizo un dump con algunos datos y luegos son cargados en la inicialización. Y para el servicio de la web se realiza el comando _runserver_ de Django para iniciar el servidor de desarrollo del mismo. 

_Explicación del funcionamiento del script iniciador_

Dicho script levanta la base de datos y hace un sleep porque suele demorar unos pocos segundos en quedar lista la base de datos, sino puede haber conflictos si se crea la web antes que la base.

Luego se copia el archivo _corbis-stock.dump_ que tiene todos los datos de prueba y se importan a la base de datos ya creada.

Finalmente se levanta el servicio de la web y ya está listo para utilizar en _localhost:8000_.

## Usuarios 
Usuario sin acceso Admin:

    user: corbisuser , pass: corbis1234


Usuario con acceso Admin:

    user: corbisadmin , pass: corbis1234

## Modelo de la Base de Datos
Es un modelo muy simple que se realizó con dos tablas, una para los Artículos y otra tabla para los Tipos de Items. Esto se hizo así ya que cuando se trata de tipos en general, es bueno hacer una tabla aparte donde estén contenidos todos los tipos. Ya que si esta tabla no estuviera entonces podría darse el caso de que, por ejemplo, se creer un item "Tecnología", otro "Tecnologia", otro "tecnologia" u otro "tecno". Entonces si se quieren filtrar sería engorroso darse de cuenta de todas las formas en las que fueron escritas. Entonces la ventaja de una tabla aparte para los tipos es que el tipo ya esta creado y cuando creo un artículo lo selecciono de los que hayan disponibles. 

## Requerimientos funcionales resueltos
1. _Como Usuario, debo poder loguearme al sistema con mi usuario y password_

    Al ingresar al sitio se pide el usuario y contraseña, puede hacerse con ambos usuarios mencionados anteriormente. Si esta mal, se pide que se vuelva a ingresar.

    Esto se resolvio utilizando el sistema de logeo propio de Django. 

2. _Como Usuario, debo tener una consola de Stock donde lista todos artículos_

    Al ingresar con un usuario correcto, se muestra una tabla con los productos creados hasta el momento. 

    Esto fue resuelto utilizando una función que levante el html principal y con un for se listan los artículos.

3. _Como Usuario, debo poder agregar un artículo al stock_

    En la barra superior hay un tag que dice _Añadir artículo_. Este redirige a un formulario realizado con los Forms de Django. Una vez realizada
    la agregación de un artículo nuevo se redirige a la página principal.

    Para poder resolver el hecho de que algunos campos sean obligatorios y otros no, es cuando se define el modelo. Para que no sea obligatorio, se define como:
        _blank = True, null = True_
    Por defecto es obligatorio tener el campo completo.

4. _Como Usuario, debo poder eliminar un artículo al stock_
    
    Se puso un botón _Borrar_ al costado de cada articulo en la lista. El mismo fue implementado con views de Django y templates, sin javascripts
    ya que no fue necesario. 

5. _Como Usuario, debo poder consultar un artículo del stock_

    Este punto en particular no entendi que es lo que se queria ya que los articulos están listados y la acción de editar es el siguiente requerimiento.
    Por lo tanto se cree que ya estaría resuelto.

6. _Como Usuario, debo poder editar un artículo del stock_

    Este método es similar al de agregar uno nuevo ya que utiliza los Forms de Django. Se agrego un botón al costado de cada artículo.
    
    Una vez hecha la modificación se redirige a la página principal.

7. _Como Administrador, debo poder gestionar USUARIOS_

    Para este punto no hubo que hacer nada ya que por defecto en el admin esta la sección para administrar los usuarios.

8. _Como Administrador, debo poder gestionar los TIPOS de Items_

    Para esto solo se tuvo que agregar en el _admin.py_ el modelo TipoItem. Además se agrego para que puedan ser editados desde la vista general y no tener que hacer clic en cada uno.

## Otros
Se creó un método que devuelve todos los artículos utilizando Django Rest Framework ya que en principio se pensó que se iba a utilizar y luego no fue necesario.

Dicho método se puede ver en _localhost:8000/api/articulos_