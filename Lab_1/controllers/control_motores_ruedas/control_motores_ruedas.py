from controller import Robot
import random


MODO_RUIDO = True

mi_robot = Robot()
paso_tiempo = int(mi_robot.getBasicTimeStep())


motor_izquierdo = mi_robot.getDevice('left wheel motor')
motor_derecho = mi_robot.getDevice('right wheel motor')  


motor_izquierdo.setPosition(float('inf'))
motor_derecho.setPosition(float('inf'))


trayectorias = ['recta', 'curva', 'circulo', 'rotacion']
indice_actual = 0
tiempo_por_etapa = 5.0 


while mi_robot.step(paso_tiempo) != -1:
    
    tiempo_actual = mi_robot.getTime()
    
    
    if tiempo_actual > (indice_actual + 1) * tiempo_por_etapa:
        if indice_actual < len(trayectorias) - 1:
            indice_actual += 1

    modo = trayectorias[indice_actual]

  
    if MODO_RUIDO:

        ruido_izq = random.uniform(-1, 1)
        ruido_der = random.uniform(-1, 1)
    else:

        ruido_izq, ruido_der = 0, 0

   
    if modo == 'recta':
        v_izq, v_der = 4.0, 4.0      # Movimiento recto (vr = vl)
    elif modo == 'curva':
        v_izq, v_der = 4.0, 2.5      # Trayectoria curva (vr != vl)
    elif modo == 'circulo':
        v_izq, v_der = 4.0, 0.8      # Círculo 
    elif modo == 'rotacion':
        v_izq, v_der = 2.0, -2.0     # Rotación (vr = -vl) 


    motor_izquierdo.setVelocity(v_izq + ruido_izq)
    motor_derecho.setVelocity(v_der + ruido_der)