import cv2 
from tkinter import *
import numpy as np
from PIL import Image,ImageTk
import imutils


#  ----------------------------------------------- Ações dos botões ---------------------------------------------------------


def visualiar():
    print("Aqui ficara a função para o recebimento das imagens")


def iniciar_CAM():

    print("Ação responsavel por iniciar a camera")

def parar_CAM():
    print("parar o exibição das cameras")

def Calibrar_CAM():
    print("Calibrando CAM.....")

def Set_values_VW():

    v = InputV.get()
    w = InputW.get()

    print("Valores V e M:")
    print("V:", v)
    print("W:", w)

def start():
    print("Inico do Jogo")

def stop():
    print("fim do jogo")

#  ---------------------------------------------------- Corpo GUI --------------------------------------------------------------


cap = None
window = Tk()
window.geometry("650x250")
window.iconbitmap('if1.ico')
window.title("VSS - Futebol de robôs")

Title_Project_Text = Label(window, 
    
    text='Interface gráfica VSS', 
    font=('arial',15,"bold")

).pack()

segundo_text = Label(window, 

    text='Camera dos robôs: ',
    font=('arial',10,"bold")

).pack(side=LEFT)

button_iniciar = Button(window, 

    text="iniciar",
    command=iniciar_CAM,

).pack(side=LEFT)

button_parar = Button(window,
    
    text="Parar", 
    command=parar_CAM, 

).pack(side=LEFT)

#Local onde será mostrado o video 
Video = Label(window)

Button_Calibração = Button(window,

    text="Calibração",
    command=Calibrar_CAM,

).pack(side=RIGHT)

Calibração_CAM_Text = Label(window,

    text="Calibração da camera: ",
    font=('arial',10,"bold"),
    justify=RIGHT

).pack(side=RIGHT)

Text_Set_VW = Label(window,

    pady=20,
    text="Set V e W:",
    justify=CENTER,
    font=('arial',10,"bold")

).pack()

InputV = Entry(window,

    textvariable="velocidade",
    width=10
    
).pack()

InputW = Entry(window,

    textvariable="velocidade Angular",
    width=10
    
).pack()

Button_Set_VW = Button(window,

    text="set values",
    command=Set_values_VW

).pack()

Button_Stop = Button(window,

    text="Stop",
    bg='red', 
    fg='white',
    width=5,
    font=('arial',10,"bold"),
    command=stop

).pack(side=BOTTOM)

Button_Start = Button(window,

    text="Start",
    bg='green', 
    fg='white',
    width=5,
    font=('arial',10,"bold"),
    command=start
    
).pack(side=BOTTOM)




window.mainloop()