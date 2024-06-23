from tkinter import *
from tkinter import ttk
import math 


root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#Funciones


def ingresarValores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        
        entrada2.set('')
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def ingresarValoresTeclado(event):
    tecla = event.char

    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        
        entrada2.set('')
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def raizCuadrada():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def borrar():
    entrada2.set(entrada2.get()[:-1])

def borrarTodo():
    entrada1.set('')
    entrada2.set('')

#Fin de funciones

# estilos

estilo_calculadora = ttk.Style()
estilo_calculadora.configure('mainframe.TFrame')
estilo_calculadora.theme_use('clam')

estilo_label_1 = ttk.Style()
estilo_label_1.configure('Label1.TLabel', font="arial 15", anchor= "e", background= "alice blue")

estilo_label_2 = ttk.Style()
estilo_label_2.configure('Label2.TLabel', font="arial 40", anchor= "e", background= "alice blue")

estilo_boton_borrar = ttk.Style()
estilo_boton_borrar.configure('boton_borrar.TButton', relief='flat', background="rosybrown1")
estilo_boton_borrar.map('boton_borrar.TButton', foreground=[('active', "#FF0000")])

estilo_bototnes_numeros = ttk.Style()
estilo_bototnes_numeros.configure('estilo_botones_numeros.TButton', relief="flat", background="aliceblue")

estilo_resto_botones = ttk.Style()
estilo_resto_botones.configure('estilo_resto_botones.TButton', relief="flat", background="azure")

estilo_boton_igual = ttk.Style()
estilo_boton_igual.configure('estilo_boton_igual.TButton', relief="flat", background="palegreen3")
estilo_boton_igual.map('estilo_boton_igual.TButton', background=[('active', "palegreen2")])

# fin de estilos

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

entrada1 = StringVar()

label_entrada_1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada_1.grid(column=0, row=0, columnspan=4 , sticky=(N, E, S, W))


entrada2 = StringVar()

label_entrada_2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada_2.grid(column=0, row=1, columnspan=4 , sticky=(N, E, S, W))


button1 = ttk.Button(mainframe, text=1, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('1'))
button0 = ttk.Button(mainframe, text=0, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('0'))
button2 = ttk.Button(mainframe, text=2, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('2'))
button3 = ttk.Button(mainframe, text=3, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('3'))
button4 = ttk.Button(mainframe, text=4, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('4'))
button5 = ttk.Button(mainframe, text=5, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('5'))
button6 = ttk.Button(mainframe, text=6, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('6'))
button7 = ttk.Button(mainframe, text=7, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('7'))
button8 = ttk.Button(mainframe, text=8, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('8'))
button9 = ttk.Button(mainframe, text=9, style='estilo_botones_numeros.TButton', command=lambda: ingresarValores('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style='boton_borrar.TButton', command=lambda: borrar()) #chr(9003) se usa para darle el simbolo de borrar
button_borrar_todo = ttk.Button(mainframe, text="C", style="estilo_resto_botones.TButton", command=lambda: borrarTodo())
button_parentesis_1 = ttk.Button(mainframe, text="(", style="estilo_resto_botones.TButton", command=lambda: ingresarValores('('))
button_parentesis_2 = ttk.Button(mainframe, text=")", style="estilo_resto_botones.TButton", command=lambda: ingresarValores(')'))
button_punto = ttk.Button(mainframe, text=".", style="estilo_resto_botones.TButton", command=lambda: ingresarValores('.'))

button_division = ttk.Button(mainframe, text=chr(247), style="estilo_resto_botones.TButton", command=lambda: ingresarValores('/'))
button_suma = ttk.Button(mainframe, text="+", style="estilo_resto_botones.TButton", command=lambda: ingresarValores('+'))
button_resta = ttk.Button(mainframe, text="-", style="estilo_resto_botones.TButton", command=lambda: ingresarValores('-'))
button_multiplicacion = ttk.Button(mainframe, text="X", style="estilo_resto_botones.TButton", command=lambda: ingresarValores('*'))

button_igual = ttk.Button(mainframe, text="=", style="estilo_boton_igual.TButton", command=lambda: ingresarValores('='))
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="estilo_resto_botones.TButton", command=lambda: raizCuadrada())

#colocar botones en pantalla

button_parentesis_1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesis_2.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_division.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S)) #con sticky le digo a que lado rellenar el espacio vacio (W(West), (E(East))) ---- Con columnspan le digo cuantas columnas ocupar
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_raiz_cuadrada.grid(column=3, row=7, sticky=(W, N, E, S))


for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<Key>', ingresarValoresTeclado)

root,mainloop()