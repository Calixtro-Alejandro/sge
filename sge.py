#from tkinter import Tk, Frame, Label, PhotoImage, Image, Entry, Button, Grid
#from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
from functools import partial
import sgeP

class Ventana:

    def BaseDeDatos():
        if dentro==1:
            Principal=Tk()

#CREA EL OBJETO DE LA CLASE DE "sgeP.py" PARA ENTRAR EN LA BASE DE DATOS
    def GUIDentroDePrincipal(self):
        print("Dentro de la pantalla principal de trabajo")
        sgeP.VentanaPrincipal(principal=None)
    
    def ConfigurarPrincipal(self):
        self.principal.title("Sistema de Gestion Empresarial")
        self.principal.resizable(1,1)
        self.principal.iconbitmap('SGE.ico')
        self.principal.config(cursor='arrow')
        self.principal.config(bg='#666666')
        self.principal.config(bd=5)
        self.principal.geometry('1200x600')

#ENTRA EN LA VENTANA PRINCIPAL Y CONECTA CON LA BASE DE DATOS
        self.GUIDentroDePrincipal()

    def ConfigurarFramePrincipal(self):
        self.frameP.config(width=1000,height=600)
        self.frameP.pack(fill='both',expand=1)
        self.frameP.config(cursor='cross')
        self.frameP.config(bg='gray')
        self.frameP.config(bd=5)
        self.GUIDentroDePrincipal()
   
#SE CONECTA CON MYSQL
    def ConeccionMySQL(self,principal=None,frameP=None):
        if self.EntryContrasena.get()=='aaa' and self.EntryUsuario.get()=='aaa':
            print("Dentro")
            messagebox.showinfo('Aviso','La clave es CORRECTA')
            self.root.destroy()
            self.principal=Tk()
            #self.frameP=Frame(principal)
            self.ConfigurarPrincipal()
            #self.ConfigurarFramePrincipal()
        else: 
            messagebox.showinfo('Aviso','La clave es incorrecta')

    def ConfigurarRoot(self):
        self.root.title("Sistema de Gestion Empresarial")
        self.root.resizable(0,0)
        self.root.iconbitmap('SGE.ico')
        self.root.config(cursor='arrow')
        self.root.config(bg='gray')
        self.root.config(bd=5)
        #self.root.geometry('600x500')

    def ConfigurarFrame(self):
        self.frame.config(width=800,height=300)
        self.frame.pack(fill='both',expand=1)
        self.frame.config(cursor='cross')
        self.frame.config(bg='gray')
        self.frame.config(bd=5)
    
    def ConfigurarLogo(self,frame=None):
        self.archivo='b1.gif'
        self.Logo=PhotoImage(file=self.archivo)
        self.lblImagen=Label(self.frame,image=self.Logo,bd=0).grid(row=0,columnspan=2,sticky=W+E)
       
    def CapturarNombre(self,frame=None):
        self.lblUsuario=Label(self.frame,text="Usuario",font=('Verdana',18),bg='gray')
        self.lblUsuario.grid(sticky='s',row=1,column=0)
        self.EntryUsuario=Entry(self.frame,font=('Verdana',18),relief='sunken',bg='gray',bd=5,justify='center')
        self.EntryUsuario.grid(row=1,column=1)    

    def CapturarClave(self,frame=None):
        self.lblContrasena=Label(self.frame,text="Clave",font=('Verdana',18),bg='gray').grid(sticky='s',row=2,column=0)    
        self.EntryContrasena=Entry(self.frame,font=('Verdana',18),relief='sunken',bg='gray',bd=5,show='*',justify='center')
        self.EntryContrasena.grid(row=2,column=1)    
 
    def CapturarBotonInicio(self,frame=None):
        self.btnEntrar=Button(self.frame,text="Entrar",font=('Verdana',18),bg='gray',command=self.ConeccionMySQL)
        self.btnEntrar.grid(row=3,column=1,sticky=W+E)    
 
    def __init__(self,root=None):
        self.root=Tk()
        self.frame=Frame(root)
        self.ConfigurarRoot()
        self.ConfigurarFrame()
        self.ConfigurarLogo()
        self.CapturarNombre()
        self.CapturarClave()
        self.CapturarBotonInicio()
        self.root.mainloop()

Ven = Ventana()
