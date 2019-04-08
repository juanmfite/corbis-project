
# Control de Stock para Test CorbisStudio

Este es un proyecto hecho en Django en el que se resuelve la consigna del test técnico.

### Especificaciones 📋

- Django 2.2
- Postgres 11.2
- Bootstrap
- Django Rest Framework
- Docker (docker-compose)

### Pre-requisitos 📋

Se debe tener instalado docker y docker-compose. 

Tener libre el puerto 8000. 

### Despliegue 🔧

Se utilizó un contenedor Docker para dicho proyecto. El mismo esta hecho con un _docker-compose_.

Para desplegar el proyecto simplemente se debe ejecutar el script _init.sh_, el mismo contiene todos los comandos de docker junto con importanción de la base de datos.

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

    En la barra superior hay un tag que dice _Añadir artículo_. Este redirige a un formulario realizado con los Forms de Django. 
    Para poder resolver el hecho de que algunos campos sean obligatorios y otros no, es cuando se define el modelo. Para que no sea obligatorio, se define como:
        _blank = True, null = True_
    Por defecto es obligatorio tener el campo completo.

4. _Como Usuario, debo poder eliminar un artículo al stock_

    En la vista se ven dos botones ya que se encaró el problema con el _Borrar2_ y se logró el funcionamiento pero el problema fue 
    que se cuando se listaban los articulos en la tabla, solo se podía usar con el primer articulos y no con el resto. Es algun
    error que no se llego a entender porque en el html. Entonces si se prueba este método se puede eliminar pero solo el primero
    de la lista. Se realizó utilizando javascript.
    
    Entonces se realizó el _Borrar_ que funciona bien pero tal vez no es una forma muy buena. Esta se realizó sin javascript, solamente
    views de Django.

5. _Como Usuario, debo poder consultar un artículo del stock_

    Este punto en particular no entendi que es lo que se queria ya que los articulos están listados y la acción de editar es el siguiente requerimiento.

6. _Como Usuario, debo poder editar un artículo del stock_

    Este método no se pudo finalizar ya que no tiraba un error cuando quería devolver la lista para editar utilizando el Form de Django.

7. _Como Administrador, debo poder gestionar USUARIOS_

    Para este punto no hubo que hacer nada ya que por defecto en el admin esta la sección para administrar los usuarios.

8. _Como Administrador, debo poder gestionar los TIPOS de Items_

    Para esto solo se tuvo que agregar en el _admin.py_ el modelo TipoItem. Además se agrego para que puedan ser editados desde la vista general y no tener que hacer clic en cada uno.

## Otros
Se creó un método que devuelve todos los artículos utilizando Django Rest Framework ya que en principio se pensó que se iba a utilizar y luego no fue necesario.

Dicho método se puede ver en _localhost:8000/api/articulos_