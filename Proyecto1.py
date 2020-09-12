from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = ""


def posTextoClick(event):
    mensaje.set(texto.index(CURRENT))
def posTextoKey(event):
    mensaje.set(texto.index(CURRENT))

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero", 
        mode="w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


# Configuración de la raíz
root = Tk()
root.geometry('900x600')
root.title("Proyecto")
menubar = Menu(root)
mensaje = StringVar() 
root.config(menu=menubar)
frame=Frame(root, width=300, height=160)
frame.pack()
root.bind('<Button-1>', posTextoClick)
root.bind('<Key>',posTextoKey)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command = nuevo)
filemenu.add_command(label="Abrir", command = abrir)
filemenu.add_command(label="Guardar", command = guardar)
filemenu.add_command(label="Guardar Como", command = guardar_como)
filemenu.add_command(label="Ejecutar Análisis")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Edición", menu=editmenu)
menubar.add_cascade(label="Herramientas", menu=filemenu)
menubar.add_cascade(label="Analizar", menu=filemenu)
menubar.add_cascade(label="Reportes", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

ventana = Frame(root)
ventana.pack(pady=5)

text_scroll = Scrollbar(ventana)
text_scroll.pack(side=RIGHT, fill=Y)
texto = Text(ventana)
texto.config(x=10, y=10,height=10, width=10)
texto.pack()
w = Label ( root,textvariable=mensaje,relief=RAISED )
w.pack()
text_scroll.config(command=texto.yview)


# Finalmente bucle de la aplicación
root.mainloop()