#Desarrollo de un  sistema de registro de pedidos por teléfono utilizando tkinter python:
# Primero escribimos tkinter para utilizar sus widgets: Tk,Label,Button y Entry.                                                           
from tkinter import Tk, Label, Button, Entry                                               
#Definir función.                                                                                            
def calcularST1():                                                                          #NOTA:

    v1 = txt7.get()                                                                         #TK:Es una interfaz
    v2 = txt8.get()                                                                         #Label:Muestra textos o imagenes
    v3 = txt11.get()                                                                        #Button:Un boton que se presiona para la ejecusión
    v4 = txt12.get()                                                                        #Entry:Es para introducir texto
    v5 = txt15.get()                                                                  #fg(foreground):Cambiar color de texto
    v6 = txt16.get()                                                                  #bg(darkgreen):Modifica color de fondo
    ST = float(v1)*float(v2)                                                          #place:Ubica elemntos como "x,y"
    txt9.delete(0,"end")                                                              #heifht:Para medir la altura que queremos de la página
    txt9.insert(0,ST)                                                                 #width: Para medir el ancho que queremos de la pagina
    ST2 = float(v3)*float(v4)                                                         #font:Fuente de letras
    txt13.delete(0,"end")
    txt13.insert(0,ST2)
    ST3 = float (v5)*float(v6)
    txt17.delete(0,"end")
    txt17.insert(0,ST3)
    T = ST + ST2 + ST3
    txt18.delete(0,"end")
    txt18.insert(0,T)
#Empieza el diseño de la página:
ventana = Tk()
ventana.geometry("600x450")
ventana.title("BOLETA ELECTRONICA")
ventana.configure(bg="#DCDCDC")
# Definir tamaño y posicion del cuadro a la vez color,tamaño y fuente de letra.
lab0 = Label(ventana,text='Ferretería El Tornillo Feliz', font=("Arial",16), fg= "#000000", bg="#DCDCDC")
lab0.place(x=170,y=10)

lab1 = Label(ventana, text='DNI: ',font=("Arial",10), fg="#000000", bg="#DCDCDC")
lab1.place(x=76,y=50, height=25)
txt1 = Entry(ventana)
txt1.place(x=110, y=53, width=70, height=25)

lab2 = Label(ventana, text='APELLIDOS: ', font=("Arial",10), fg="#000000" , bg="#DCDCDC")
lab2.place(x=28, y=90)
txt2 = Entry(ventana)
txt2.place(x=110,y=92, width=130, height=25)

lab3 = Label(ventana, text='NOMBRES: ' ,font=("Arial",10), fg="#000000" ,bg="#DCDCDC")
lab3.place(x=302,y=90)
txt3 = Entry(ventana)
txt3.place(x=380,y=92, width=130, height=25)

lab4 = Label(ventana, text='DIRECCION: ', font=("Arial",10), fg="#000000", bg="#DCDCDC")
lab4.place(x=28, y=130)
txt4 = Entry(ventana)
txt4.place(x=110, y=132, width=350, height=25)

lab5 = Label(ventana, text='TELELEFONO: ', font=("Arial",10), fg="#000000", bg="#DCDCDC")
lab5.place(x=13, y=170)
txt5 = Entry(ventana)
txt5.place(x=110, y=170, width=350, height=25)

lab6 = Label(ventana, text='Codigo de producto', font=("Arial",11), fg="#000000", bg="#DCDCDC")
lab6.place(x=20, y=210)

lab7 = Label(ventana, text='Descripcion', font=("Arial",11), fg="#000000", bg="#DCDCDC")
lab7.place(x=160, y=210)

lab8 = Label(ventana, text='Unidad', font=("Arial",11), fg="#000000", bg="#DCDCDC")
lab8.place(x=260, y=210)

lab9 = Label(ventana, text='Cantidad', font=("Arial",11), fg="#000000", bg="#DCDCDC")
lab9.place(x=340, y=210)

lab10= Label(ventana, text='Precio', font=("Arial",11), fg="#000000", bg="#DCDCDC")
lab10.place(x=430, y=210)

lab11 = Label(ventana, text='Subtotal', font=("Arial",11), fg="#000000", bg="#DCDCDC")
lab11.place(x=500, y=210)

txt6 = Entry(ventana)
txt6.place(x=40,y=250,width=70, height=25)
txt7 = Entry(ventana)
txt7.place(x=349,y=250,width=40, height=25)
txt8 = Entry(ventana)
txt8.place(x=423,y=250,width=60, height=25)
txt9 = Entry(ventana)
txt9.place(x=498,y=250,width=65, height=25)
txt10 = Entry(ventana)

txt10.place(x=40,y=280,width=70, height=25)
txt11 = Entry(ventana)
txt11.place(x=349,y=280,width=40, height=25)
txt12 = Entry(ventana)
txt12.place(x=423,y=280,width=60, height=25)
txt13 = Entry(ventana)
txt13.place(x=498,y=280,width=65, height=25)

txt14 = Entry(ventana)
txt14.place(x=40,y=310,width=70, height=25)
txt15 = Entry(ventana)
txt15.place(x=349,y=310,width=40, height=25)
txt16 = Entry(ventana)
txt16.place(x=423,y=310,width=60, height=25)
txt17 = Entry(ventana)
txt17.place(x=498,y=310,width=65, height=25)

#Boton para calcular el total;
btn = Button(ventana, text='Calcular Total', font=("Arial",11),command = calcularST1, bg="#DCDCDC", fg="#000000")
btn.place(x=190, y=350)
#Boton para información:
btn2 = Button(ventana, text='Información', font=("Arial",11),command =  calcularST1,bg="#DCDCDC", fg="#000000")
btn2.place(x=95, y=350)
#Boton para limpiar:
btn3 = Button(ventana, text='Limpiar', font=("Arial",11),command = calcularST1, bg="#DCDCDC", fg="#000000")
btn3.place(x=30, y=350)

lab12 = Label(ventana,text='TOTAL: ', font=("Arial",11), fg="#000000", bg="#DCDCDC")
lab12.place(x=428,y=350)
txt18 = Entry(ventana)
txt18.place(x=498, y= 350, width=65, height=25)

#Una forma mas sencilla para ver el resultado de la creación de la página se copia en el IDLE de python y se ejecuta.


    
