Automatización de imágenes Sentinel-2 

¡Hola! Este proyecto nace desde la necesidad de poder simplificar el manjeo de la información contenida en las imagenes satelitales de la constelacion -Sentinel-.
Cuando trabajamos con una gran cantidad de datos particularmente en sotware especializados, puede resultar engorroso y complicado, además del tiempo invertido y lo lento que puede ser. 
En algunos casos necesitamos usar una parte especifica de la inforamción, no su totalidad. Por lo tanto el objetivo de este proyecto es automatizar la extraccion de las carpetas principales, generando una nueva estructura de archivos 
con la información más relevante, evitando perdida de tiempo. 

¿Por qué está bueno este proyecto? (¡al menos eso creo yo!)
*Ahorramos tiempo
*Simplificamos los procesos
*Estructuramos la información según nuestras necesidades.
*Es fácil de usar ya que solo hay que modificar los directorios.

Requisito:

Versión de Python: a partir de Python 3.9
Biblioteca: "Os", "Shutil"

¿Cómo usar el código?

Copia el código o descárgalo desde el repositorio:
[https://github.com/VitaNM/Automatizaci-n_im-genes_Sentinel2.git](https://github.com/VitaNM/Automatizaci-n_im-genes_Sentinel2.git).

Si usas un entorno como Anaconda o Visual Studio Code, asegúrate de tener instaladas las bibliotecas `os` y `shutil` (vienen con Python, no necesitas instalarlas por separado)

Configura las rutas

Es importante recordar antes de ejecutar el script que pongas las direcciones/rutas de forma correcta.
→ ruta_origen colocar la ruta donde están las imágenes.
→ ruta_destino colocar la ruta donde van a ir las carpetas organizadas.

Antes de ejecutar el código las carpetas tienen esta estrcutura:
C:\Users\User\Desktop\
2023
octubre
S2A_MSIL2A_20231001T123456_N1234_R123_T12ABC_20231001T123456.SAFE
S2A_MSIL2A_20231001T123456_N1234_R123_T12ABC_20231001T123456
GRANULE
AUX_DATA
IMG_DATA
QI_DATA\

Luego de ejecutar el codigo deberían verse con esta estructura:
C:\Users\User\Desktop\
octubre
S2A_MSIL2A_20231001T123456_N1234_R123_T12ABC_20231001T123456_nuevo
AUX_DATA
IMG_DATA
QI_DATA\

Si querés personalizarlo,  ajusta o modifica las variables en el script
Si necesitas otra información solo se modifican algunas variables y listo!

¡Todas las sugerenicas y las contribuciones son muy bienvenidas!

Recorda hacer:
-Un fork del repositorio 
-Create una rama con tu contribución
-Hace un pull request para revisar los cambios!

¡Espero que tambien sea útil para ustedes!

Este proyecto está bajo la licencia MIT. 
