
import tkinter as tk
from tkinter import CENTER, DISABLED, Label, PhotoImage
import random

vent = tk.Tk()
vent.geometry('550x700')

vent.title('Piedra, papel o tijera')
vent.config(bg='gainsboro')

def botones_estado():
    if (bott_papel['state'] and bott_piedra['state'] and bott_tijera['state'] == tk.DISABLED):
        bott_papel['state']  = tk.NORMAL
        bott_piedra['state'] = tk.NORMAL
        bott_tijera['state'] = tk.NORMAL
    else:
        return


############################### imagenes #######################################
imagen1= PhotoImage(file=r"C:\Users\kevin\Documents\Piedra, papel o tijera\ppt2.png")
imagen2= PhotoImage(file=r"C:\Users\kevin\Documents\Piedra, papel o tijera\ppt1.png")
portada= Label(vent,image=imagen1).grid(row=0, column=2, pady=10)
manos= Label(vent, image=imagen2).grid(row=8, column=2, rowspan=2)


############################### Etiquetas de texto #############################
eti_1 = tk.Label(vent, text='Juego de Piedra, Papel o Tijera', font = ('Candara', 15), bg='gainsboro')
eti_1.grid(row=1, column=2, pady=10)

eti_2 =tk.Label(vent, text='Teclea tu nombre, por favor', bg='gainsboro')
eti_2.grid(row=2, column=2)

eti_3 = tk.Label(vent, text='Da clic la opcion que desees.', bg='gainsboro')
eti_3.grid(row=5, column=2, pady=10)

eti_4 = tk.Label(vent, text='Computadora', font = ('Candara', 15), bg='gainsboro')
eti_4.grid(row=8, column=3, pady= 10)



##############################  nombre del jugador #############################
ent_nom = tk.Entry(vent, font='Helvetica 10', justify = 'center', bd=5)
ent_nom.grid(row=3, column=2)

############################## display del jugador #############################
nom_jugador = tk.Text(vent, font = ('Candara', 10), bg = 'white', fg = 'black', width=15, height=1, bd=3)
nom_jugador.grid(row=8, column=1)

def captura():  ### funcion con la que se captura el nombre tipeado, se inserta en el display del contador, se elimina del espacio de tipeado y de desabilita el boton de "listo"
    nombre = ent_nom.get()
    nom_jugador.insert(tk.END, nombre)
    ent_nom.delete(0,'end')    
    bott_nombre['state'] = tk.DISABLED

############################## boton del nombre ###############################
bott_nombre = tk.Button(text='¡¡Listo!!', font= ('Candara', 10), bd=3, activebackground='darkkhaki', command = lambda:[captura(), botones_estado()]) #### Con lambda se asegura que el boton active varias funciones a la vez 
bott_nombre.grid(row=4, column=2, pady=10)



############################## display principal del juego #####################
respuesta = tk.Text(vent, font = ('Helvetica', 10), bg = 'black', fg = 'yellow', width=70, height=3, bd=3)
respuesta.grid(row=7, column=1, pady=20, columnspan=3)


########### Displays de contadores de partidas #########
cont_jugador = tk.Text(vent, font = 'Helvetica 10', bg = 'black', fg = 'yellow', width=10, height=2)
cont_jugador.grid(row=9, column=1)

cont_compu = tk.Text(vent, font = 'Helvetica 10', bg = 'black', fg = 'yellow', width=10, height=2)
cont_compu.grid(row=9, column=3)


########## boton de reinicio ##########}
bott_reinicio = tk.Button(text='Reiniciar el contador', font= ('Candara', 10), bd=3, activebackground='darkkhaki')
bott_reinicio.grid(row=10, column=2, pady=20)


#######################################################################
opciones= ['piedra', 'papel', 'tijera']
jugador = ''
#################### Funcion para eleccion de la computadora ##########
def eleccion_compu(opciones):
    for opcion in opciones:
        compu = random.choice(opciones)
    return compu
    
#######################################################################
###################### Funcion para eleccion del jugador ##############
def piedra():
    jugador = 'piedra'    
    juego(opciones, jugador)    

def papel():
    jugador = 'papel'
    juego(opciones, jugador) 

def tijera():
    jugador = 'tijera'
    juego(opciones, jugador) 

#######################################################################
##################### Funcion del Juego ###############################

def juego(opciones, jugador):
    respuesta.delete(0.0, tk.END)      
    computadora = eleccion_compu(opciones)
    
    if jugador == computadora:        
        resulado1 ='Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora + '\nEs un empate'
        respuesta.insert(tk.END, resulado1)

    elif jugador == 'piedra' and computadora == 'tijera':        
        resultado2 = 'Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora + '\nHas ganado'
        respuesta.insert(tk.END, resultado2)

    elif jugador == 'papel' and computadora == 'piedra':        
        resultado3 = 'Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora + '\nHas ganado'
        respuesta.insert(tk.END, resultado3)

    elif jugador == 'tijera' and computadora =='papel':        
        resultado4 = 'Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora + '\nHas ganado' 
        respuesta.insert(tk.END, resultado4)

    else:
        resultado5 ='Has escogido '+ jugador + ' y la computadora ha escogido ' + computadora + '\nHas perdido'
        respuesta.insert(tk.END, resultado5)
           

############################# Botones de opciones #############################
bott_piedra = tk.Button(text='Piedra', font= ('Candara', 10), width=10, bd=3, activebackground='darkkhaki', command= piedra, state=tk.DISABLED)
bott_piedra.grid(row=6, column=1, padx=30)

bott_papel = tk.Button(text='Papel', font= ('Candara', 10), width=10, bd=3, activebackground='darkkhaki', command= papel, state=tk.DISABLED)
bott_papel.grid(row=6, column=2)

bott_tijera= tk.Button(text= 'Tijera', font= ('Candara', 10), width=10, bd=3, activebackground='darkkhaki', command= tijera, state=tk.DISABLED)
bott_tijera.grid(row=6, column=3, padx= 30)



vent.mainloop()