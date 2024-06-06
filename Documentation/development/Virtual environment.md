Este proyecto trabaja bajo un entorno virtual creado bajo la biblioteca virtualenv, para hacer uso de esta, se hace una instalación con pip siguiente el siguiente comando en la consola de comandos de windows o el powershell:

```
pip install virtualenv 
```

Una vez instalada esta biblioteca, se ejecutará una ventana de comandos del sistema dentro de la carpeta asignada para el proyecto y se creará el entorno virtual de la siguiente manera:

```
virtualenv -p python3 nombre_de_entorno
```

(La carpeta del entorno virtual de este proyecto se ubicará en la carpeta raíz de SAMICA-Project, nombrada como "venv"), para poder trabajar en este proyecto y sus respectivas dependencias, deberá ser activado el entorno virtual antes de cualquier cambio, para esto se utilizará el siguiente comando:

```
.\venv\Scripts\activate
```

Esto activará el entorno virtual dentro de nuestro editor de código, y podremos trabajar tranquilamente sobre nuestro proyecto SAMICA.

NOTA: Recordar que los primeros 2 códigos solo con un ejemplo de creación de un venv, sin embargo, para trabajar con el proyecto actual, se necesitará realizar anteriormente una copia de este repositorio y hacer uso del último código mostrado.
