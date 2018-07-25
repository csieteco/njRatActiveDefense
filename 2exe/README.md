## 2exe folder

Archivos creados con el fin de crear un ejecutable que además presentar un documento PDF ejecute un script que ejecuta otras acciones en "segundo plano". El ataque busca hacer uso de un archivo SFX generado con WinRAR.

### Archivos

* *launch.vbs* - Contiene la instrucción para que en su ejecución no se observe la ventana de comandos, ejecutará el script pdf.bat.
* *pdf.bat* - Script que contiene las instrucciones para ejecutar el archivo legítimo que se desea mostrar, seguido de las instrucciones que se llevarán en "segundo plano". Los archivos que llama [pdf.bat](pdf.bat), njratAWS.exe y Documento.pdf (archivo que se supone es el legítimo y observará la víctima), no están incluídos ya que variará según el uso que se desee dar.
* *http.bat* - Script que permite conexiones HTTP, buscando garantizar el envío de información a nuestro [servidor](../server.py)
* *newPDFicon.ico* - Ícono usado para ser usado por el ejecutable que se generará.

### Creación

Se debe de abrir WinRAR y añadir los archivos, luego se deberá elegir la opción "auto-extraíble". Se habilitará la opción de configuración avanzada en la que se deberá indicar que el archivo *launch.vbs* será ejecutado luego de la extracción. Se recomienda seleccionar la extracción en una carpeta temporal y elegir un ícono acorde al archivo que se pretende suplantar.
