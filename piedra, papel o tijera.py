#Prueba de piedra, papel o tijera

import random

opciones = ['piedra', 'papel', 'tijera']

#######################################################################
### Funcion para eleccion de la computadora ###
def eleccion_compu(opciones):
    for opcion in opciones:
        compu = random.choice(opciones)
    return compu
    
#######################################################################
### Funcion para eleccion del jugador ###
def eleccion_jugador(opciones):
    eleccion = (input('Elige tu opcion: Piedra, papel o tijera: ').lower())    
    if eleccion not in opciones:
        print('No has seleccionado un opcion valida')
        repeticion()                       
    else:        
        return eleccion    
    
#######################################################################
### Funcion del Juego ###

def juego(opciones):
    jugador = eleccion_jugador(opciones)
    computadora = eleccion_compu(opciones)

    if jugador == computadora:
        print('Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora)
        print('Es un empate')
    elif jugador == 'piedra' and computadora == 'tijera':
        print('Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora)
        print('Has ganado')
    elif jugador == 'papel' and computadora == 'piedra':
        print('Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora)
        print('Has ganado')
    elif jugador == 'tijera' and computadora =='papel':
        print('Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora)
        print('Has ganado')
    else:
        print('Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora)
        print('Has perdido')

    repeticion()

def repeticion():
    rep = (input('¿Deseas jugar otra vez? (s/n) ').lower())
    if rep == 's':
        juego(opciones)
    else:
        print('Juego cerrado, adios')

juego(opciones)
