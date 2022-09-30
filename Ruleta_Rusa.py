import PySimpleGUI as sg 
import time 
import os
import random

#======================================================================================#
#Para que las funciones de apagar la pc se apliquen, necesitas remover el simbolo de '#'
#======================================================================================#

time_duration = 10
spin = random.randint(1,6)

start = sg.popup_get_text('Quieres jugar? Si o No?', 'Ruleta Rusa')
sg.popup('Ruleta Rusa', 'Tu respuesta fue: ', start)

if start == 'Si' or start == 'SI' or start == 'si' or start == 's' or start == 'S':
    try:
        if spin == 1:
            sg.popup('Perdiste tines 10 segundos para guardar tus archivos')
            time.sleep(time_duration)
            #os.system('shutdown /s /t 1')
            sg.popup('Acá se apaga la pc perro compento la función para que no se me apague durante las pruebas')

        else:
            sg.popup('Bala perdida, te salvaste')
            #Acá podemos hacer que se apague aun que hayamos ganado en la ruleta
            sg.popup('No importa tienes 10 segundos para guardar todo antes de que se apague')
            time.sleep(time_duration)
            #os.system('shutdown /s /t 1')
            sg.popup('Acá se apaga la pc')

    except Exception as error:
        print(error)

else:
    sg.popup('No le saque', 'Ruleta Rusa')


