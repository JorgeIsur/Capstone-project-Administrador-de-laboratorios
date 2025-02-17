# PN532-Raspberry pi model B+
### Lector de sensor NFC (PN532) con raspberry
## INSTRUCCIONES 
### CONFIGURACIÓN SENSOR
Colocar el sensor en el modo MSU, para esto debemos de mover el dipswitch. En este caso como es modo MSU, colocamos el 1 en OFF y el 2 en OFF. (También nos podemos guiar viendo la tabla del sensor, esta se encuentra a un lado del dipswitch como se puee ver en la siguiente imagen) 

<img src = "https://github.com/ElierRosales/Capstone-project-Administrador-de-laboratorios/blob/1591fc57af5bbe840283c8702dcfac98775471e2/PN532/Imagenes%20PN532/DIP-SWITCH-I_PN532.jpg" width="500">

### CONEXIÓN DEL SENSOR A RASPBERRY

| Pin en el modulo NFC | Pin Raspberry |
| -- | -- |
| GND | 6 |
| VCC | 2 |
| SDA | 10 |
| SCL | 8 |

Nota: Esto podría cambiar dependiendo de tu modelo de Raspberry.

#### Diagrama esquematico de conexiones 

<img src = "https://github.com/ElierRosales/Capstone-project-Administrador-de-laboratorios/blob/7dad47193bc19ab89996144e0be6fb12bbd2f054/PN532/Imagenes%20PN532/PN532-PI.png" width="500">

### INSTALACIÓN DE BIBLIOTECAS Y MODULOS QUE SE UTILIZAN
* Abrimos la terminal y revisamos si tenemos y que versión de Python tenemos instalado con :

  `python --version`

   en caso de no tenerlo instalado, podemos instalarlo con:
 
  `sudo apt-get install python3`

* Revisamos si tenemos las ultimas actualizaciones disponibles, para esto colocamos lo siguiente:

  `sudo apt update && sudo apt upgrade`

* Instalamos el modulo PN532pi de Python que vamos a utilizar con la instrucción :

  `sudo pip3 install pn532pi`

* Instalamos el modulo paho de Python que es el que nos permitirá realizar la conexión MQTT:

  `pip3 install paho-mqtt` 
      
  en caso de que no lo permita, usamos `sudo` antes de la instrucción.
  
* Ahora vamos a probar un código, escribimos lo siguiente en la terminal:

   `cd Documents` 

 `git clone https://github.com/ElierRosales/Capstone-project-Administrador-de-laboratorios.git`
 
  entramos en la carpeta PN532 la cual encontraremos dentro de nuestra carpeta Documents, abrimos el archivo UIDporMQTT.py
  con Thony Python IDE y damos en el botón Run.
  Ahora pasamos un tag NFC y en consola se imprimirá el UID de tu tag.
 







