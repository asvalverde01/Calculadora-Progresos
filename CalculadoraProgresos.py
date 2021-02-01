#Unversidad de las Américas
#Proyecto final primer semestre
#Calculadora de progresos
#Desarollado por Sebastian Valverde

from tkinter import*

#Definicion de funciones
#La funcion calculo1() lee las tres notas ingresadas para calcular el promedio
#   Muestra un mensaje segun la nota obtenida
def calculo1():
    try:
        nota1 = float(get1.get())
        nota2 = float(get2.get())
        nota3 = float(get3.get())
        resultado = ((nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.40))

        if resultado >= 6:
            result.configure(text = "La nota promedio es: {:.2f}".format(resultado))
        else:
            result.configure(text = "La nota promedio es: {:.2f}".format(resultado))
    except:
        result.configure(text = "Ingrese los datos necesarios")
        resultStatus.configure(text = "---Operación Fallida---")
    else:
        resultStatus.configure(text = "---Operación Exitosa---")
    
#La funcion calculo2() lee las dos notas ingresadas para calcular el promedio necesario para sacar 6
#   Muestra un mensaje segun la nota obtenida
def calculo2():
    try:
        nota4 = float(get4.get())
        nota5 = float(get5.get())
        resultado = ((nota4 * 0.25) + (nota5 * 0.35))

        if resultado >= 6:
            result.configure(text = "Nota para pasar alcanzada :)")
        else:
            tot = 6 - resultado
            tot = (tot * 10)/4
            result.configure(text="Se requiere una nota de:  {:.2f}".format(tot))
    except:
        result.configure(text = "Ingrese los datos necesarios")
        resultStatus.configure(text = "---Operación Fallida---")
    else:
        resultStatus.configure(text = "---Operación Exitosa---")

def ayuda():
    try:
        ayudaGUI = Tk()
        ayudaGUI.title("Acerca de")
        text1a = Label(ayudaGUI, font=('Consolas', 13),
                        text = "ESTE PROGRAMA HA SIDO DESSAROLLADO POR\n"
                        "Alberto Sebastián Valverde Gonzalez\n"
                        "para el proyecto final de la clase de algoritmos")
        
        contactos = LabelFrame(ayudaGUI, font=('Consolas', "13", 'bold'), text = "CONTACTOS")
        text2a = Label(contactos, font=('Consolas', 13),
                        text = "Correo institucional:\n")
        correo = Entry(contactos, font=('Consolas', '12'), width= 32, borderwidth= 5, 
            justify="center", fg="black")
        correo.insert(END, "sebastian.valverde@udla.edu.ec")


        
        text1a.grid(row = 1)
        contactos.grid(row = 2)
        text2a.grid(row = 3)
        correo.grid(row = 4)
        ayudaGUI.mainloop()
    except:
        resultStatus.configure(text = "---Operación Fallida---")

def borrar():
    get1.delete(0, END)
    get2.delete(0, END)
    get3.delete(0, END)
    get4.delete(0, END)
    get5.delete(0, END)
    result.configure(text = "-----<>-----")
    resultStatus.configure(text = "- - - Campos borrados - - -")

#Inicio de la interfaz
root = Tk()
root.title("Calculadora de nota progresos UDLA -- por Sebastian Valverde")

#Menu y sus opciones 
menuBar = Menu(root)
root.config(menu = menuBar)

helpmenu = Menu(menuBar, tearoff = 0)
helpmenu.add_command(label = "Acerca de", command = ayuda)
menuBar.add_cascade(label =  "Ayuda", menu = helpmenu)

clear = Menu(menuBar, tearoff = 0)
clear.add_command(label = "Borrar Todo", command = borrar)
menuBar.add_cascade(label =  "Borrar campos", menu = clear)


#Informacion sobre el programa presentada en la parte superior
saludo = Label(root, bg="#00678B",
    fg="red", 
    font=('Consolas', '20', 'bold'), 
    width=40, text="-UNIVERSIDAD DE LAS AMERICAS-")\
    .grid(row=0, column=1)

saludo1 = Label(root, bg="#00678B", 
    fg="white", 
    font=('Consolas', '20', 'bold'), 
    width=40, text="--CALCULADORA DE PROGRESOS--")\
    .grid(row=1, column=1)


#Texto y recoleccion de datos primera seccion
frame1 = LabelFrame(root, font=('Consolas', '17', 'bold') , text="En caso de conocer las\n"
                               " 3 notas, use esta sección", bg="#00678B", fg="white")

text1 = Label(frame1, font=('Consolas', '17') , bg="#00678B" , 
                text="\nIngrese la primera nota: ").grid(row= 6, column= 0)
text2 = Label(frame1, font=('Consolas', '17') , bg="#00678B" , 
                text="\nIngrese la segunda nota: ").grid(row= 8, column= 0)
text3 = Label(frame1, font=('Consolas', '17') , bg="#00678B" , 
                text="\nIngrese la tercera nota: ").grid(row= 10, column= 0)

get1 = Entry(frame1, font=('Consolas', '16', 'bold'), width= 8, borderwidth= 8, 
                bg="#00CC00", justify="center", fg="black")
get2 = Entry(frame1, font=('Consolas', '16', 'bold'), width= 8, borderwidth= 8, 
                bg="#00CC00", justify="center", fg="black")
get3 = Entry(frame1, font=('Consolas', '16', 'bold'), width= 8, borderwidth= 8, 
                bg="#00CC00", justify="center", fg="black")


#Texto y recoleccion de datos segunda seccion
frame2 = LabelFrame(root, font=('Consolas', '17', 'bold') , text="En caso de conocer\n"
                                                         " solamente 2 notas\n"
                               "use esta sección", bg="#00678B", fg="white")

text4 = Label(frame2, font=('Consolas', '17') , bg="#00678B" , text="\nIngrese la primera nota:")\
    .grid(row= 6, column= 2)
text5 = Label(frame2, font=('Consolas', '17') , bg="#00678B" , text="\nIngrese la segunda nota:")\
    .grid(row= 8, column= 2)

get4 = Entry(frame2, font=('Consolas', '16', 'bold'), width= 8, borderwidth= 8, 
            bg="#00CC00", justify="center", fg="black")
get5 = Entry(frame2, font=('Consolas', '16', 'bold'), width= 8, borderwidth= 8, 
            bg="#00CC00", justify="center", fg="black")


#Seccion  central con resultados y botones
frame3 = LabelFrame(root, font=('Consolas', '16', 'bold') , text="Resultados", bg="#00678B", fg="white")

text6 = Label(frame3, font=('Consolas', '17') , bg="#00678B" , 
                text="\nPresione el boton para:").grid(row= 6, column= 1)

button_1 = Button(frame3, font=('Consolas', '16', 'bold'), borderwidth=5, text="Calcular nota final", padx=50,
                pady=6, bg="#00CC00",command = calculo1)

text7 = Label(frame3, font=('Consolas', '17') , bg="#00678B" , 
                text="\nPresione el boton para:").grid(row= 8, column= 1)

button_2 = Button(frame3, font=('Consolas', '16', 'bold'), borderwidth=5, text="Calcular nota necesaria", padx=34,
                pady=6, bg="#00CC00", command = calculo2)

text7 = Label(frame3, font=('Consolas', '14', 'bold') , bg="#00678B" , 
                text="--------<RESULTADO>--------", fg="white").grid(row= 10, column= 1)

result = Label(frame3, width=30, font=('Consolas', '18', 'bold') , borderwidth=10, justify="center", bg="#00678B",
                text= "-----<>-----")

resultStatus = Label(frame3, width=30, font=('Consolas', '13', 'bold'), borderwidth=10, justify="center", 
                bg="#00678B", fg="white", text= "----<>----")

#En esta seccion se muestra las instrucciones del programa
instru = LabelFrame(root, font=('Consolas', '17',  'bold') , text="Instrucciones", bg="#00678B", fg="white")
instruLin = Label(instru, font=('Consolas', '13') , text="Este programa ha sido desarollado con la "
                                                         "metodología de calificación de la UDLA\n"
                                                         "-----------------------------------------------------------\n"
                                                         "Progreso 1 = %25     |     Progreso 2 = %35"
                                                         "     |     Progreso 3 = %40\n"
                                                         "-----------------------------------------------------------\n"
                                                         "Si conoce las 3 notas, por favor, use la seccion izquierda.\n"
                                                         "Si conoce 2 notas, por favor, use la seccion derecha "
                                                         "para calcular nota necesaria.", bg="#00678B")


#Zona izquierda
frame2.grid(row= 5, column = 2)
get4.grid(row = 7, column = 2)
get5.grid(row = 9, column = 2)

#Zona central
frame3.grid(row= 5, column = 1)
button_1.grid(row = 7, column = 1)
button_2.grid(row = 9, column = 1)
result.grid(row = 11, column = 1)
resultStatus.grid(row = 12, column = 1)

#Zona derecha
frame1.grid(row= 5, column = 0)
get1.grid(row = 7, column = 0)
get2.grid(row = 9, column = 0)
get3.grid(row = 11, column = 0)

#Zona instrucciones
instru.grid(row= 14, columnspan = 3 )
instruLin.grid(row= 17)

#Sentencia repetiviva que permite ejecutar el programa
root.configure(bg="#00678B")
root.resizable(0,0)
root.mainloop()