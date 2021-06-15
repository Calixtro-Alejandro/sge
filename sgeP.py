#from tkinter import Tk, Frame, Label, PhotoImage, Image, Entry, Button, Grid
#from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
#from sge import *
from tkinter import ttk
import sgeN
import Controlador

#import mysql.connector

class VentanaPrincipal:

    def ConexionMYSQL(self):
        #try:
            #import mysql.connector
        #except ImportError:
            #raise ImportError('Se requiere el modulo mysql.connector')
        #print("Intentando conectar con la base de datos")
        #self.MiConexion=mysql.connector.connect(host='magazinte.com',user='magazint_BDD_SGE_USER',passwd='S5d+h$mCdbQb',database='magazint_BDD_SGE')
        #self.MiConexion=mysql.connector.connect(host='localhost',user='root',passwd='', database='test')
        #print(self.MiConexion)
        #print(type(self.MiConexion))
        sgeN.sgeBDD(MiConexion=None)

#MOSTRAR LISTA DE NOMINAS 
    def MostrarLisNom(self):
        #sgeN.sgeBDD(MiConexion=None)
        Controlador.ControladorBDD.ConVerNom(self)


#LIMPIAR CAMPOS
    def LimpiarCampos(self):
        self.dentroNombre.set("")
        self.dentroGenero.set("")
        self.dentroArea.set("")
        self.dentroRol.set("")
        self.dentroSalario.set("")
        self.dentroNumeroSeguro.set("")
        self.dentroCorreoElectronico.set("")
        self.dentroClave.set("")
        self.dentroNumeroTelefono.set("")

#MOSTRAR LOS DATOS YA GUARDADOS DEL USUARIO NUEVO
    def MostrarDatos(self):
        print("Mostrar datos del usuario nuevo guardado")

#BOTON GUARDAR NUEVO USUARIO
    def GuardarDarUsu(self):
        print("Intentando guardar datos del usuario nuevo")
        #Controlador.ControladorBDD.ConNueUsu(self,self.dentro)
        
#DATOS DE USUARIO PARA ENVIAR AL CONTROLADODR
    #NOMBRE
        self.NomNombre=self.dentroNombre.get()
    #GENERO
        self.NomGenero=self.dentroGenero.get()
    #AREA
        self.NomArea=self.dentroArea.get()
    #ROL
        self.NomRol=self.dentroRol.get()
    #SALARIO
        self.NomSalario=self.dentroSalario.get()
    #NUMERO DE DEGURO
        self.NomNumeroSeguro=self.dentroNumeroSeguro.get()
    #CORREO ELECTRONICO
        self.NomCorreoElectronico=self.dentroCorreoElectronico.get()
    #CLAVE
        self.NomClave=self.dentroClave.get()
    #NUMERO DE TELEFONO
        self.NomNumeroTelefono=self.dentroNumeroTelefono.get()

        Controlador.ControladorBDD.ConNueUsu(self,self.NomNombre,self.NomGenero,self.NomArea,self.NomRol,self.NomSalario,self.NomNumeroSeguro,self.NomCorreoElectronico,self.NomClave,self.NomNumeroTelefono)

        #print('IDE: '+str(self.Nom))
        print('Nombre: '+str(self.NomNombre))
        print('Genero: '+str(self.NomGenero))
        print('Area: '+str(self.NomArea))
        print('Rol: '+str(self.NomRol))
        print('Salario: '+str(self.NomSalario))
        print('Numero de seguro: '+str(self.NomNumeroSeguro))
        print('Correo electronico: '+str(self.NomCorreoElectronico))
        print('Clave: '+str(self.NomClave))
        print('Numero de telefono: '+str(self.NomNumeroTelefono))

        print('El ususario se guardo, se proceden a limpiar campos')

        self.LimpiarCampos()

        self.MostrarDatos()

#VENTANA PARA AGREGAR NUEVOS USUARIOS

    def NuevoUsuario(self):
        #self.dentroNombre=StringVar()
        self.dentroNombre=StringVar()
        self.dentroGenero=StringVar()
        self.dentroArea=StringVar()
        self.dentroRol=StringVar()
        self.dentroSalario=StringVar()
        self.dentroNumeroSeguro=StringVar()
        self.dentroCorreoElectronico=StringVar()
        self.dentroClave=StringVar()
        self.dentroNumeroTelefono=StringVar()

        #print(self.dentroNombre)
        
        self.venNueUsu=Toplevel()
        self.venNueUsu.geometry('400x600')
        self.venNueUsu.iconbitmap('SGE.ico')

#widgets internos
        self.lblFoto=Label(self.venNueUsu,text="FOTO")
        self.lblFoto.grid(row=0, columnspan=2,sticky=W+E)

#OBLIGATORIOS PARA LA EMPRESA
    #LABEL
        self.lblID=Label(self.venNueUsu,text="ID")
        self.lblID.grid(row=1, column=0)
        self.lblNombre=Label(self.venNueUsu,text="Nombre")
        self.lblNombre.grid(row=2, column=0)
        self.lblGenero=Label(self.venNueUsu,text="Genero")
        self.lblGenero.grid(row=3, column=0)
        self.lblArea=Label(self.venNueUsu,text="Area")
        self.lblArea.grid(row=4, column=0)
        self.lblRol=Label(self.venNueUsu,text="Rol")
        self.lblRol.grid(row=5, column=0)
        self.lblSalario=Label(self.venNueUsu,text="Salario")
        self.lblSalario.grid(row=6, column=0)
        self.lblNumSeg=Label(self.venNueUsu,text="Numero de seguro")
        self.lblNumSeg.grid(row=7, column=0)
        self.lblCorEle=Label(self.venNueUsu,text="Correo electronico")
        self.lblCorEle.grid(row=8, column=0)
        self.lblClave=Label(self.venNueUsu,text="Clave")
        self.lblClave.grid(row=9, column=0)
        self.lblNumTel=Label(self.venNueUsu,text="Numero de telefono")
        self.lblNumTel.grid(row=10, column=0)
        self.lblSeparador=Label(self.venNueUsu,text="--------------------")
        self.lblSeparador.grid(row=11, column=0)

#OBLIGATORIOS PARA LA EMPRESA 
    #ENTRY
        self.lblNumID=Label(self.venNueUsu,text='xxxxxxxxxxxx')
        self.lblNumID.grid(row=1,column=1)
        self.EntNombre=ttk.Entry(self.venNueUsu,textvariable=self.dentroNombre)
        self.EntNombre.grid(row=2,column=1)
        self.EntNombre.focus()

        vcbGenero=["Masculuno","Femenino"]
        self.comBoxGenero=ttk.Combobox(self.venNueUsu,values=vcbGenero,textvariable=self.dentroGenero)
        self.comBoxGenero.set("Genero")
        self.comBoxGenero.grid(row=3,column=1)

        vcbArea=["Gerencia","Ventas","Mantenimiento"]
        self.comBoxArea=ttk.Combobox(self.venNueUsu,values=vcbArea,textvariable=self.dentroArea)
        self.comBoxArea.set("Selecciona el area")
        self.comBoxArea.grid(row=4,column=1)
        
        vcbRol=["Gerente","Mesero","Cajero"]
        self.comBoxRol=ttk.Combobox(self.venNueUsu,values=vcbRol,textvariable=self.dentroRol)
        self.comBoxRol.set("Selecciona el rol")
        self.comBoxRol.grid(row=5,column=1)

        self.EntSalario=Entry(self.venNueUsu,textvariable=self.dentroSalario)
        self.EntSalario.grid(row=6,column=1)
        self.EntNumSeg=Entry(self.venNueUsu,textvariable=self.dentroNumeroSeguro)
        self.EntNumSeg.grid(row=7,column=1)
        self.EntCorEle=Entry(self.venNueUsu,textvariable=self.dentroCorreoElectronico)
        self.EntCorEle.grid(row=8,column=1)
        self.EntClave=Entry(self.venNueUsu,textvariable=self.dentroClave)
        self.EntClave.grid(row=9,column=1)
        self.EntNumTel=Entry(self.venNueUsu,textvariable=self.dentroNumeroTelefono)
        self.EntNumTel.grid(row=10,column=1)
#BOTON GUARDAR NUEVO USUARIO
        self.btnGuardarUsu=Button(self.venNueUsu,text='Guardar',command=self.GuardarDarUsu)
        self.btnGuardarUsu.grid(row=1,column=3)

#DATOS PERSONALES
    #LABEL
        self.lblPeso=Label(self.venNueUsu,text="Peso")
        self.lblPeso.grid(row=12,column=0)
        self.lblEstatura=Label(self.venNueUsu,text="Estatura")
        self.lblEstatura.grid(row=13,column=0)
        self.lblTipSangre=Label(self.venNueUsu,text="Tipo de sangre")
        self.lblTipSangre.grid(row=14,column=0)
        self.lblAlergias=Label(self.venNueUsu,text="Alergias")
        self.lblAlergias.grid(row=15,column=0)

        #self.btnAgrCam=Button(self.venNueUsu,text="Agregar campo")
        #self.btnAgrCam.grid(row=16,column=0)

#DATOS PERSONALES
    #ENTRY
        self.EntPeso=Entry(self.venNueUsu)
        self.EntPeso.grid(row=12,column=1)          
        self.EntEstatura=Entry(self.venNueUsu)
        self.EntEstatura.grid(row=13,column=1)
        self.EntTipSangre=Entry(self.venNueUsu)
        self.EntTipSangre.grid(row=14,column=1)
        self.EntAlergias=Entry(self.venNueUsu)
        self.EntAlergias.grid(row=15,column=1)

        #self.EntAgrCam=Entry(self.venNueUsu)
        #self.EntAgrCam.grid(row=16,column=1)
        

    def FrameExtra(self):    
        self.frmE=Frame(self.frameP)
        self.frmE.config(width=200,height=400)
        self.frmE.pack(side='right',fill='y',expand=0)
        self.frmE.config(cursor='cross')
        self.frmE.config(bg='#626262')
        self.frmE.config(bd=0)
        

    def LisInv(self):
        self.lblArea=Label(self.FrmI,text='Areas: ')
        self.lblArea.grid(row=0,column=0)

        vlist=["Gerencia","Ventas","Mantenimiento","Produccion"]
        self.cbArea=ttk.Combobox(self.FrmI,values=vlist)
        self.cbArea.set("Seleccion de areas")
        self.cbArea.grid(row=0,column=1)

        self.btnNueArea=Button(self.FrmI,text='Agregar nueva area')
        self.btnNueArea.grid(row=0,column=3)

        self.btnQuiArea=Button(self.FrmI,text='Eliminar area')
        self.btnQuiArea.grid(row=0,column=4)

        self.lisBI=Listbox(self.FrmI)
        self.lisBI.insert(1,"Manzanas")
        self.lisBI.insert(2,"Aguacates")
        self.lisBI.grid(row=1,columnspan=5,sticky=W+E)

    def LisNom(self):

        self.FrmNom=Frame(self.FrmN)
        self.FrmNom.config(width=800,height=600)
        self.FrmNom.pack(side='left',fill='y',expand=0)
        self.FrmNom.config(cursor='cross')
        self.FrmNom.config(bg='gray')
        self.FrmNom.config(bd=0)

#WIDGETS DE LA PESTAÑA DE NOMINAS
        self.lblNueEmp=Label(self.FrmNom,text='FOTO')
        self.lblNueEmp.grid(rowspan=2,columnspan=2,sticky=W+E)
        self.btnNueEmp=Button(self.FrmNom,text='Nuevo',command=self.NuevoUsuario)
        self.btnNueEmp.grid(row=3,column=0)
        self.btnQuiEmp=Button(self.FrmNom,text='Eliminar empleado')
        self.btnQuiEmp.grid(row=3,column=1)

#PESTANAS DENTRO DE LA PESTANA DE RH

        #panel Recursos Humanos
        pnlRH=ttk.Notebook(self.FrmN)
        pnlRH.pack(fill='both',expand="yes")

        #FRAME EMPLEADOS
        self.FrmRHN=Frame(pnlRH,bg='gray',bd=0)
        #self.FrmRHN.config(width=400,height=400)
        self.FrmRHN.pack(side='left',fill='y',expand=0)
        #FRAME PROVEDORES
        self.FrmRHP=Frame(pnlRH,bg='gray',bd=0)
        self.FrmRHP.pack(fill='both',expand=1)
        #FRAME OUTSOURSING
        self.FrmRHO=Frame(pnlRH,bg='gray',bd=0)
        self.FrmRHO.pack(fill='both',expand=1)
        #FRAME CLIENTES
        self.FrmRHC=Frame(pnlRH,bg='gray',bd=0)
        self.FrmRHC.pack(fill='both',expand=1)

        #NOMINAS
        pnlRH.add(self.FrmRHN,text="Nominas")
        #PROVEDORES
        pnlRH.add(self.FrmRHP,text="Provedores")
        #OUTSORSING
        pnlRH.add(self.FrmRHO,text="Outsorsing")
        #CLIENTES
        pnlRH.add(self.FrmRHC,text="Clientes")



#LISTA DE LA BASE DE DATOS DE NOMINAS
        #self.lisBN=Listbox(self.FrmRHN)
        #self.lisBN.insert(1,"Fulano")
        #self.lisBN.insert(2,"Mengano")
        #self.lisBN.pack(fill='both',expand=1)

        self.lisBN=ttk.Treeview(self.FrmRHN,selectmode='browse',
                height=10,columns=('#0','#1','#2',
                    '#3','#4','#5',
                    '#6','#7','#8','#9'))
        self.lisBN.pack(fill='both',expand=1)

        self.lisBNScrolbarY=ttk.Scrollbar(self.lisBN,orient="vertical",
                command=self.lisBN.yview)
        self.lisBNScrolbarY.pack(side='right',fill='both')

        self.lisBNScrolbarX=ttk.Scrollbar(self.lisBN,orient="horizontal",
                command=self.lisBN.xview)
        self.lisBNScrolbarX.pack(side='bottom',fill='both')


        self.lisBN.column('#0',width=100)
        self.lisBN.heading('#0',text="ID",anchor=CENTER)
        self.lisBN.heading('#1',text="Nombres",anchor=CENTER)
        self.lisBN.heading('#2',text="Genero",anchor=CENTER)
        self.lisBN.column('#2',width=100)
        self.lisBN.heading('#0',text="ID",anchor=CENTER)
        self.lisBN.heading('#3',text="Area",anchor=CENTER)
        self.lisBN.heading('#4',text="Rol",anchor=CENTER)
        self.lisBN.heading('#5',text="Salario",anchor=CENTER)
        self.lisBN.heading('#6',text="Numero de seguro",anchor=CENTER)
        self.lisBN.heading('#7',text="Correo electronico",anchor=CENTER)
        self.lisBN.heading('#8',text="Clave",anchor=CENTER)
        self.lisBN.heading('#9',text="Numero de telefono",anchor=CENTER)
        
        #Controlador.ControladorBDD.ConVerNom(self)

        #self.lisBN.insert('',0,text="nombre",values=datos)
        
#LISTA DE LA BASE DE DATOS DE PROVEDORES
        self.lisBN=Listbox(self.FrmRHP)
        self.lisBN.insert(1,"Fulano")
        self.lisBN.insert(2,"Mengano")
        self.lisBN.pack(fill='both',expand=1)
#LISTA DE LA BASE DE DATOS DE OTSORSING
        self.lisBN=Listbox(self.FrmRHO)
        self.lisBN.insert(1,"Fulano")
        self.lisBN.insert(2,"Mengano")
        self.lisBN.pack(fill='both',expand=1)
#LISTA DE LA BASE DE DATOS DE CLIENTES
        self.lisBN=Listbox(self.FrmRHC)
        self.lisBN.insert(1,"Fulano")
        self.lisBN.insert(2,"Mengano")
        self.lisBN.pack(fill='both',expand=1)

#MOSTRAR LISTA DE NOMINAS
        self.MostrarLisNom()

    def Paneles(self):
        
        #panel
        pnl=ttk.Notebook(self.frameP)
        pnl.pack(fill='both',expand="yes")

        #FRAME ESTADISTICAS
        self.FrmE=Frame(pnl,bg='gray',bd=0)
        self.FrmE.config(width=800,height=600)
        self.FrmE.pack(side='left',fill='y',expand=0)
        #FRAME VENTAS
        self.FrmV=Frame(pnl,bg='gray',bd=0)
        self.FrmV.pack(fill='both',expand=1)
        #FRAME INVENTARIOS
        self.FrmI=Frame(pnl,bg='gray',bd=0)
        self.FrmI.pack(fill='both',expand=1)
        #FRAME NOMINAS
        self.FrmN=Frame(pnl,bg='gray',bd=0)
        self.FrmN.pack(fill='both',expand=1)

        #ESTADISTICAS
        pnl.add(self.FrmE,text="Estadisticas")
        #VENTAS
        pnl.add(self.FrmV,text="Ventas")
        #INVENTARIOS
        pnl.add(self.FrmI,text="Inventarios")
        #NOMINAS
        pnl.add(self.FrmN,text="RH")

        #LABEL DE TABS
        #lbf=ttk.Label(FrmE, text="hola",bg='gray')
        #lbf=ttk.Label.grid(row=0,column=0)

    def btnConectarAMySQL(self, frameP=None):
        self.btnConectar=Button(self.frameP,text="Conectar",command=self.ConexionMYSQL)
        #self.btnConectar.pack()
        self.btnConectar.grid(row=0,columnspand=5,sticky=W+E)

    def FrameVentanaPrincipal(self,principal=None):
        self.frameP=Frame(principal)
        self.frameP.config(width=1000,height=600)
        self.frameP.pack(fill='both',expand=1)
        self.frameP.config(cursor='cross')
        self.frameP.config(bg='#626262')
        self.frameP.config(bd=0)
        
        self.FrameExtra()

        self.Paneles()
        
        self.LisInv()

        self.LisNom()
        
    def btnConectarAMySQL(self, frameP=None):
        self.btnConectar=Button(self.frameP,text="Conectar",command=self.ConexionMYSQL)
        #self.btnConectar.pack()
        self.btnConectar.grid(row=0,column=0)

        self.frameP.config(width=1200,height=600)
    
    def __init__(self,principal=None):
        self.ConexionMYSQL()
        self.FrameVentanaPrincipal(principal)
