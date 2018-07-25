# njratCounterAttack

### Info

El archivo server.py sirve para registrar todas las peticiones recibidas, es útil en combinación con los post que hace el .bat que está en 2exe.

La versión sobre la que se trabaja es la 0.7d de njRat.

### El ataque

El ataque documentado, consiste en subir un archivo malicioso que tiene apariencia de documento PDF, esperando a que el atacante lo ejecute y de esa forma pueda ejecutar el payload generado. La idea en definitiva es lograr la ubicación del atacante extrayendo las conexiones WiFi cercanas. También intentar aplicar la misma técnica de *njrat* para controlarlo desde el propio C&C.

Tener muy presente el separador que se usa en el protocolo de comunicaciones del troyano. El script de identificación, permite sacar el separador del C&C, para luego usarlo en el script. Se puede automatizar también esta parte para que el script de ataque reconozca antes de lanzar el separador.

### TODO

Encontrar una técnica directa que permita ejecutar código sobre el C&C del atacante.
