from pyfirmata import Arduino, util
from tkinter import *
from time import sleep

root = Tk()
root.geometry('800x520')
root.configure(bg='white')
root.title("Arduuno")

timepo = [0,0,0]

cont = 0
init = False

segundos = str(timepo[0])
minutos = str(timepo[1])
hora = str(timepo[2])

texto = Label(root, 
                text= hora + ":" + minutos + ":" + segundos, 
                bg='blue', 
                font=("Arial Bold", 40), 
                fg="yellow")
texto.grid(padx=10, pady=10,column=0, row=0)


def parar ():
    print("paro")
    global init
    init = False

def inicio ():
    print("inicio")
    global init
    init = True

def cerrar ():
    root.destroy()

def reiniciar ():
    global timepo
    global cont
    print("reinicio")
    timepo[0] = 0
    timepo[1] = 0
    timepo[2] = 0
    cont = 0

def clock ():
    global timepo
    global cont 
    sleep(0.1)
    cont += 1
    if(cont == 10):
        timepo[0]+=1
        cont = 0
    if(timepo[0] == 60):
        timepo[1] +=1
        timepo[0] = 0
    if(timepo[1] == 60):
        timepo[1] = 0
        timepo[2] +=1

def mostrar():
    global texto
    global segundos,minutos,hora
    global timepo

    segundos = str(timepo[0])
    minutos = str(timepo[1])
    hora = str(timepo[2])

boton = Button(root,
    text = "Iniciar",
    command = inicio,
    bg = 'maroon4'
)
boton.grid(column = 2, row = 0)

boton = Button(root,
    text = "Parar",
    command = parar,
    bg = 'maroon4'
)
boton.grid(column = 3, row = 0)

boton = Button(root,
    text = "Cerrar",
    command = cerrar,
    bg = 'maroon4'
)
boton.grid(column = 4, row = 0)

boton = Button(root,
    text = "Reiniciar",
    command = reiniciar,
    bg = 'maroon4'
)
boton.grid(column = 5, row = 0)

while(1):
    root.update()
    if(init):
        clock()
    mostrar()
    texto.configure(text = str(hora) + str(":") + str(minutos) + str(":") + str(segundos))
    

#root.mainloop()