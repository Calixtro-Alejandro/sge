#from tkinter import Tk, Frame, Label, PhotoImage, Image, Entry, Button, Grid
#from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
#from sge import *
from tkinter import ttk

class sgeBDD:

#SE CREAN LAS BASES DE DATOS PERTINENTES POR DEFAULT

    def CrearBDDRecursosHumanos(self):
        print("Crear bases de datos de RECUSSOS HUMANOS")
        import mysql.connector
        miConexion=mysql.connector.connect(host='localhost', user='root',passwd='')
        cursor1=miConexion.cursor()
        
        try:
            cursor1.execute('create database bddrecursoshumanos') 
        except:
            print("No se pudo crear la base de datos de 'RECUSSOS HUMANOS'")
            miConexion.rollback()
        miConexion.close()

    def CrearBDDInventarios(self):
        print("Crear bases de datos de INVENTARIOS")
        import mysql.connector
        miConexion=mysql.connector.connect(host='localhost', user='root',passwd='')
        cursor1=miConexion.cursor()
        
        try:
            cursor1.execute('create database bddinventarios') 
        except:
            print("No se pudo crear la base de datos de 'INVENTARIOS'")
            miConexion.rollback()
        miConexion.close()

    def CrearBDDVentas(self):
        print("Crear bases de datos de VENTAS")
        import mysql.connector
        miConexion=mysql.connector.connect(host='localhost', user='root',passwd='')
        cursor1=miConexion.cursor()
        
        try:
            cursor1.execute('create database bddventas') 
        except:
            print("No se pudo crear la base de datos de 'VENTAS'")
            miConexion.rollback()
        miConexion.close()

    def CrearBDDEstadisticas(self):
        print("Crear bases de datos de ESTADISTICAS")
        import mysql.connector
        miConexion=mysql.connector.connect(host='localhost', user='root',passwd='')
        cursor1=miConexion.cursor()
        
        try:
            cursor1.execute('create database bddestadisticas') 
        except:
            print("No se pudo crear la base de datos de 'ESTADISTICAS'")
            miConexion.rollback()
        miConexion.close()

#SE CREAN LAS TABLAS PERTINENTES PARA RECURSOS HUMANOS
    def CrearTablasNominas(self):
        print("Inrentando crear tablas para BDD de RH")
        import mysql.connector
        miConexion=mysql.connector.connect(host='localhost', user='root',passwd='',database='bddrecursoshumanos')
        cursor1=miConexion.cursor()
        
        try:
            cursor1.execute('CREATE TABLE IF NOT EXIST nominas(ide int(13) NOT NULL, nombre varchar(50) NOT NULL, genero varchar(50) NOT NULL, area varchar(50) NOT NULL, rol varchar(50) NOT NULL, salario varchar(50) NOT NULL, numeroseguro varchar(50) NOT NULL, correoelectronico varchar(50) NOT NULL, clave varchar(50) NOT NULL, numerotelefono varchar(50) NOT NULL)')


            print("Intentando crear la tabla para ptovedores")
            cursor1.execute('CREATE TABLE IF NOT EXIST provedores(ide int(13) NOT NULL, nombre varchar(50) NOT NULL, area varchar(50) NOT NULL, rol varchar(50) NOT NULL, correoelectronico varchar(50) NOT NULL, numerotelefono varchar(50) NOT NULL)')







            miConexion.commit()
        except:
            print("No se pudo crear la tabla de 'NOMIMAS'")
            miConexion.rollback()
        miConexion.close()


#MOSTRAR LISTA DE NOMINAS
    def MostrarBDD(self,MiConexion):

        import mysql.connector

        #self.MiConexion=mysql.connector.connect(host='magazinte.com',user='magazint_BDD_SGE_USER',passwd='S5d+h$mCdbQb',database='magazint_BDD_SGE')

        print("Intenta mostrar las base de datos")

        self.MiConexion=mysql.connector.connect(host='localhost',user='root',passwd='')
        
        self.cursor1=self.MiConexion.cursor()

        try:
            self.cursor1.execute('show databases')
        except:
            print("No se pudo ejecutar el comando 'show databases'")
            self.MiConexion.rollback()
        
        for x in self.cursor1:
            print(x)
        self.MiConexion.close()

    def __init__(self,MiConexion=None):
        self.CrearBDDRecursosHumanos()
        self.CrearBDDInventarios()
        self.CrearBDDVentas()
        self.CrearBDDEstadisticas()
        
        self.CrearTablasNominas()

        self.MostrarBDD(MiConexion)
