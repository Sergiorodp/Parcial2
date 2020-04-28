from pyfirmata import Arduino, util
from tkinter import *
from time import sleep

root = Tk()
root.geometry('800x960')
root.configure(bg='white')
root.title("punto2")

sizex_circ = 40
sizey_circ = 40


placa = Arduino('COM3')
it = util.Iterator(placa)
it.start()


pin_led1 = placa.get_pin('d:13:o')
pin_led2 = placa.get_pin('d:12:o')
pin_led3 = placa.get_pin('d:11:o')
pin_led4 = placa.get_pin('d:10:o')
pin_led5 = placa.get_pin('d:9:o')
pin_led6 = placa.get_pin('d:8:o')

draw = Canvas(root, width=800, height=600)
draw.place(x = 0,y = 0)

led1_draw=draw.create_oval(10,10,10+sizex_circ,10+sizey_circ,fill="white")
led2_draw=draw.create_oval(75,10,75+sizex_circ,10+sizey_circ,fill="white") 
led3_draw=draw.create_oval(140,10,140+sizex_circ,10+sizey_circ,fill="white")
led4_draw=draw.create_oval(205,10,205+sizex_circ,10+sizey_circ,fill="white")
led5_draw=draw.create_oval(270,10,270+sizex_circ,10+sizey_circ,fill="white")
led6_draw=draw.create_oval(335,10,335+sizex_circ,10+sizey_circ,fill="white")

def luces(valor):

    dato = int(valor)
    print(dato)
    if(dato < 20):
        draw.itemconfig(led1_draw, fill = 'yellow')
        draw.itemconfig(led2_draw, fill = 'white')
        draw.itemconfig(led3_draw, fill = 'white')
        draw.itemconfig(led4_draw, fill = 'white')
        draw.itemconfig(led5_draw, fill = 'white')
        draw.itemconfig(led6_draw, fill = 'white')

        pin_led1.write(1)
        pin_led2.write(0)
        pin_led3.write(0)
        pin_led4.write(0)
        pin_led5.write(0)
        pin_led6.write(0)

    if(dato >= 20 and dato < 40):
        draw.itemconfig(led1_draw, fill = 'yellow')
        draw.itemconfig(led2_draw, fill = 'blue')
        draw.itemconfig(led3_draw, fill = 'white')
        draw.itemconfig(led4_draw, fill = 'white')
        draw.itemconfig(led5_draw, fill = 'white')
        draw.itemconfig(led6_draw, fill = 'white')

        pin_led1.write(1)
        pin_led2.write(1)
        pin_led3.write(0)
        pin_led4.write(0)
        pin_led5.write(0)
        pin_led6.write(0)

    if(dato >= 40 and dato < 60):
        draw.itemconfig(led1_draw, fill = 'yellow')
        draw.itemconfig(led2_draw, fill = 'blue')
        draw.itemconfig(led3_draw, fill = 'green')
        draw.itemconfig(led4_draw, fill = 'white')
        draw.itemconfig(led5_draw, fill = 'white')
        draw.itemconfig(led6_draw, fill = 'white')

    
        pin_led1.write(1)
        pin_led2.write(1)
        pin_led3.write(1)
        pin_led4.write(0)
        pin_led5.write(0)
        pin_led6.write(0)

    if(dato >= 60 and dato < 80):
        draw.itemconfig(led1_draw, fill = 'yellow')
        draw.itemconfig(led2_draw, fill = 'blue')
        draw.itemconfig(led3_draw, fill = 'green')
        draw.itemconfig(led4_draw, fill = 'red')
        draw.itemconfig(led5_draw, fill = 'white')
        draw.itemconfig(led6_draw, fill = 'white')
        
        
        pin_led1.write(1)
        pin_led2.write(1)
        pin_led3.write(1)
        pin_led4.write(1)
        pin_led5.write(0)
        pin_led6.write(0)

    if(dato >= 80 and dato < 100):
        draw.itemconfig(led1_draw, fill = 'yellow')
        draw.itemconfig(led2_draw, fill = 'blue')
        draw.itemconfig(led3_draw, fill = 'green')
        draw.itemconfig(led4_draw, fill = 'red')
        draw.itemconfig(led5_draw, fill = 'yellow')
        draw.itemconfig(led6_draw, fill = 'white')

        
        pin_led1.write(1)
        pin_led2.write(1)
        pin_led3.write(1)
        pin_led4.write(1)
        pin_led5.write(1)
        pin_led6.write(0)

    if(dato >= 100 and dato < 120):
        draw.itemconfig(led1_draw, fill = 'yellow')
        draw.itemconfig(led2_draw, fill = 'blue')
        draw.itemconfig(led3_draw, fill = 'green')
        draw.itemconfig(led4_draw, fill = 'red')
        draw.itemconfig(led5_draw, fill = 'yellow')
        draw.itemconfig(led6_draw, fill = 'green')

        
        pin_led1.write(1)
        pin_led2.write(1)
        pin_led3.write(1)
        pin_led4.write(1)
        pin_led5.write(1)
        pin_led6.write(1)

w1 = Scale(root,command = luces,from_=0,length=335 ,to=120, tickinterval=10, orient = HORIZONTAL)
#w1.set(lectura1)
w1.pack()
w1.place(x = 0, y = 50)

root.mainloop()

