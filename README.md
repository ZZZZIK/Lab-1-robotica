# Lab-1-robotica
Laboratorio 1: Simulacion de un Robot Movil
Diferencial en Webots
Objetivo
Comprender el comportamiento cinematico de un robot movil diferencial mediante una simulacion interactiva en Webots, donde los actuadores
(motores de las ruedas) controlan el movimiento del robot.

Introduccion
Un robot movil diferencial utiliza dos ruedas motrices independientes
ubicadas a cada lado del robot. El movimiento depende de las velocidades de
cada rueda.
En este laboratorio se utilizara Webots para simular el robot y observar
como las velocidades de las ruedas determinan su movimiento.


Instrucciones para ejecutar la simulacion en Webots:

Pasos previos a la ejecucion: Instalar Python(version 3.10 o superior) y Webots.


Paso 1: Descargar los archivos del repositorio de Github
Paso 2: Ejecutar Webots 
Paso 3: Dar click en File y abrir la carpeta "Lab1" seguir la ruta Lab1->worlds->laboratorio_1.wbt
Paso 4: Una vez cargado el archivo, darle click al icono de la carpeta que se encuentra sobre la terminal de la derecha (open existing text file) y seguir la ruta lab1->controllers->control_motores_ruedas->control_motores_ruedas.py
Paso 5: Cambiar el valor de "MODO_RUIDO =" a True o False segun quiera observar el comportamiento.
Paso 6: Iniciar la simulacion usando los controles de pausa, resumen, rebobinar, etc.

Resultados obtenidos:
-Se pudo observar un notorio cambio en la trayectoria del Robot al modificar el valor de Ruido para cada rueda, pues provoco movimientos erraticos sin seguir la trayectoria predefinida.
-Al modificar la velocidad de las ruedas de manera que sean desiguales, el robot va a girar hacia el lado de la rueda con velocidad mas baja.
-Si omitimos el ruido y dejamos las ruedas con igual velocidad, el robot se mueve en linea recta.
-Si las velocidades de ambas ruedas son un numero y su inverso aditivo respectivamente, el robot va a girar sobre su propio eje.
