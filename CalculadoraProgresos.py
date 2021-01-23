#Unversidad de las Américas
#Proyecto final primer semestre
#Calculadora de progresos
#Desarollado por Sebastian Valverde

from tkinter import*

#Definicion de funciones
def calculo1():
    nota1 = float(get1.get())
    nota2 = float(get2.get())
    nota3 = float(get3.get())
    resultado = ((nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.40))
    result.configure(text = "La nota promedio es: {:.2f}".format(resultado))

def calculo2():
    nota4 = float(get4.get())
    nota5 = float(get5.get())
    resultado = ((nota4 * 0.25) + (nota5 * 0.35))

    if resultado >= 6:
        result.configure(text = "Nota para pasar alcanzada :)")

    else:
        tot = 6 - resultado
        tot = (tot * 10)/4
        result.configure(text="Se requiere una nota de: "+ str(tot))


def fun_clear():
    result.delete(0, END)



root = Tk()
root.title("Calculadora de progresos")

#Informacion sobre el programa presentada en la parte superior
saludo = Label(root, bg="#00FF80", font=('Consolas', '15', 'bold'), width=40, text="---UNIVERSIDAD DE LAS AMERICAS---")\
    .grid(row=0, column=1)
saludo1 = Label(root, bg="#00FF80", font=('Consolas', '15', 'bold'), width=40, text="----CALCULADORA DE PROGRESOS----")\
    .grid(row=1, column=1)
informacion = Label(root, bg="#00FF80", font=('Consolas', '13'), width=40, text="Bienvenido! Usa esta calculadora\n "
                                                                               "para calcular promedio o predecir \n"
                                                                                "la nota que necesitas para pasar.")\
.grid(row=3, column=1)




#Texto y recoleccion de datos primera seccion
frame1 = LabelFrame(root, font=('Consolas', '13', 'bold') , text="En caso de conocer las 3 notas\n"
                               "use esta sección", bg="#00FF80")

text1 = Label(frame1, font=('Consolas', '12') , bg="#00FF80" , text="\nIngrese la primera nota: ")\
    .grid(row= 6, column= 0)
text2 = Label(frame1, font=('Consolas', '12') , bg="#00FF80" , text="\nIngrese la segunda nota: ")\
    .grid(row= 8, column= 0)
text3 = Label(frame1, font=('Consolas', '12') , bg="#00FF80" , text="\nIngrese la tercera nota: ")\
    .grid(row= 10, column= 0)

get1 = Entry(frame1, width= 10, borderwidth= 8, bg="#00CC00", justify="center", fg="black")
get2 = Entry(frame1, width= 10, borderwidth= 8, bg="#00CC00", justify="center", fg="black")
get3 = Entry(frame1, width= 10, borderwidth= 8, bg="#00CC00", justify="center", fg="black")


#Texto y recoleccion de datos segunda seccion
frame2 = LabelFrame(root, font=('Consolas', '13', 'bold') , text="En caso de conocer\n"
                                                         " solamente 2 notas\n"
                               "use esta sección", bg="#00FF80")

text4 = Label(frame2, font=('Consolas', '12') , bg="#00FF80" , text="\nIngrese la primera nota: ")\
    .grid(row= 6, column= 2)
text5 = Label(frame2, font=('Consolas', '12') , bg="#00FF80" , text="\nIngrese la segunda nota: ")\
    .grid(row= 8, column= 2)


get4 = Entry(frame2, width= 10, borderwidth= 8, bg="#00CC00", justify="center", fg="black")
get5 = Entry(frame2, width= 10, borderwidth= 8, bg="#00CC00", justify="center", fg="black")

instru = LabelFrame(root, font=('Consolas', '12',  'bold') , text="Instrucciones", bg="#00FF80")
#instruL = Label(instru, font=('Consolas', '10') , text="                                           "
     #                                                  "                                           "
   #                                                    "                                           ", bg="#00FF80")
instruLin = Label(instru, font=('Consolas', '10') , text="Este programa ha sido desarollado con la "
                                                         "metodología de calificación de la UDLA\n"
                                                         "-----------------------------------------------------------\n"
                                                         "Progreso 1 = %25     |     Progreso 2 = %35"
                                                         "     |     Progreso 3 = %40\n"
                                                         "-----------------------------------------------------------\n"
                                                         "Si conoce las 3 notas, por favor, use la seccion izquierda.\n"
                                                         "Si conoce 2 notas, por favor, use la seccion derecha "
                                                         "para calcular nota necesaria.", bg="#00FF80")


#Seccion de resultados
frame3 = LabelFrame(root, font=('Consolas', '13', 'bold') , text="Resultados", bg="#00FF80")

text6 = Label(frame3, font=('Consolas', '12') , bg="#00FF80" , text="\nPresione para calcular el progreso:")\
    .grid(row= 6, column= 1)

button_1 = Button(frame3, font=('Consolas', '10', 'bold'), borderwidth=5, text="Calcular nota final", padx=50,
                  pady=6, fg="Black", bg="#00CC00",command = calculo1)

text7 = Label(frame3, font=('Consolas', '12') , bg="#00FF80" , text="\nPresione para calcular el progreso:")\
    .grid(row= 8, column= 1)

button_2 = Button(frame3, font=('Consolas', '10', 'bold'), borderwidth=5, text="Calcular nota necesaria", padx=38,
                  pady=6, fg="Black", bg="#00CC00", command = calculo2)

text7 = Label(frame3, font=('Consolas', '12') , bg="#00FF80" , text="------RESULTADO------")\
    .grid(row= 10, column= 1)

result = Label(frame3, width=30, font=('Consolas', '13', 'bold'), borderwidth=10, justify="center", bg="#00FF80",
                fg="black")\



#----------
frame1.grid(row= 5, column = 0)
get1.grid(row = 7, column = 0)
get2.grid(row = 9, column = 0)
get3.grid(row = 11, column = 0)

frame2.grid(row= 5, column = 2)
get4.grid(row = 7, column = 2)
get5.grid(row = 9, column = 2)

frame3.grid(row= 5, column = 1)

instru.grid(row= 12, columnspan=3 )
#instruL.pack()
instruLin.grid(row= 13, columnspan = 2)

button_1.grid(row=7, column=1)
button_2.grid(row=9, column=1)
result.grid(row= 11, column= 1)
#Sentencia repetiviva que permite ejecutar el programa
root.configure(bg="#00FF80")
root.resizable(0, 0)
root.mainloop()