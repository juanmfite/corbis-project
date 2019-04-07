
# Control de Stock para Test CorbisStudio

Este es un proyecto hecho en Django en el que se resuelve la consigna del test técnico.

### Pre-requisitos 📋

Se debe tener instalado docker y docker-compose. Además se debe tener libre el puerto 8000, es el utilizado por Django por defecto por su servidor de prueba. 

### Instalación 🔧

Se utilizó un contenedor Docker para dicho proyecto. El mismo esta hecho con un _docker-compose_.

Para desplegar el proyecto simplemente se debe ejecutar el script _init.sh_, el mismo contiene todos los comandos de docker junto con importanción de la base de datos.

_Funcionamiento del script iniciador_
Dicho script levanta la base de datos y hace un sleep porque suele demorar unos pocos segundos, sino puede haber conflictos si se crea la web antes que la base de datos.
Luego se copia el archivo _corbis-stock.dump_ que tiene todos los datos de prueba y se importan a la base de datos ya creada.
Luego se levanta el servicio de la web y ya está listo para utilizar en _localhost:8000_.

## Usuarios 
Usuario sin acceso Admin:
    user: _corbisuser_ , pass: _corbis1234_
Usuario con acceso Admin:
    user: _corbisadmin_ , pass: _corbis1234_

## Modelo de la Base de Datos
Es un modelo muy simple que se realizó con dos tablas, una para los Artículos y otra tabla para los Tipos de Items. Esto se hizo así ya que cuando se trata de tipos en general, es bueno hacer una tabla aparte donde estén contenidos todos los tipos. Ya que si esta tabla no estuviera entonces podría darse el caso de que, por ejemplo, se creer un item "Tecnología", otro "Tecnologia", otro "tecnologia" u otro "tecno". Entonces si se quieren filtrar sería engorroso darse de cuenta de todas las formas en las que fueron escritas. Entonces la ventaja de una tabla aparte para los tipos es que el tipo ya esta creado y cuando creo un artículo lo selecciono de los que hayan disponibles. 

## Requerimientos funcionales resueltos
1. Como Usuario, debo poder loguearme al sistema con mi usuario y password

Al ingresar al sitio se pide el usuario y contraseña, puede hacerse con ambos usuarios mencionados anteriormente. Si esta mal, se pide que se vuelva a ingresar.

Esto se resolvio utilizando el sistema de logeo propio de Django. 

2. Como Usuario, debo tener una consola de Stock donde lista todos artículos

Al ingresar con un usuario correcto, se muestra una tabla con los productos creados hasta el momento. 

Esto fue resuelto utilizando una función que levante el html principal y con un for se listan los artículos.

3. Como Usuario, debo poder agregar un artículo al stock

En la barra superior hay un tag que dice _Añadir artículo_. Este redirige a un formulario realizado con los Forms de Django. 
Para poder resolver el hecho de que algunos campos sean obligatorios y otros no, es cuando se define el modelo. Para que no sea obligatorio, se define como:
    _blank = True, null = True_
Por defecto es obligatorio tener el campo completo.

4. Como Usuario, debo poder eliminar un artículo al stock

Para eliminar esto se agrego un butón al costado de cada articulo para que pueda ser borrado

5. Como Usuario, debo poder consultar un artículo del stock

Este punto en particular no entendi que es lo que se queria ya que los articulos están listados y la acción de editar es el siguiente requerimiento.

6. Como Usuario, debo poder editar un artículo del stock

7. Como Administrador, debo poder gestionar USUARIOS

Para este punto no hubo que hacer nada ya que por defecto en el admin esta la sección para administrar los usuarios.

8. Como Administrador, debo poder gestionar los TIPOS de Items

Para esto solo se tuvo que agregar en el _admin.py_ el modelo TipoItem. Además se agrego para que puedan ser editados desde la vista general y no tener que hacer clic en cada uno.