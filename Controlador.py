#from tkinter import Tk, Frame, Label, PhotoImage, Image, Entry, Button, Grid
#from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
#from sge import *
from tkinter import ttk

class ControladorBDD:

    def ConNueUsu(self,NomNombre,NomGenero,NomArea,NomRol,NomSalario,NomNumeroSeguro,
            NomCorreoElectronico,NomClave,NomNumeroTelefono):
        print("Crear dtos para NUEVO USUARIO")
        import mysql.connector
        miConexion=mysql.connector.connect(host='localhost', user='root',passwd='',
                database='bddrecursoshumanos')
        cursor1=miConexion.cursor()
        print("esta dentro la data: " + NomNombre)
        #datos=ide_.get()
        #print(str(ide_))

        nombre_=NomNombre
        genero_=NomGenero
        area_=NomArea
        rol_=NomRol
        salario_=NomSalario
        numeroseguro_=NomNumeroSeguro
        correoelectronico_=NomCorreoElectronico
        clave_=NomClave
        numerotelefono_=NomNumeroTelefono

        miSQL='INSERT INTO nominas (id, nombre, genero, area, rol, salario, numeroseguro, correoelectronico, clave, numerotelefono) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        valores=('1',nombre_,genero_,area_,rol_,salario_,numeroseguro_,correoelectronico_,
                clave_,numerotelefono_)

        #valores={'id_':'00001','nombre_':'alejandro romo hernandez','genero_':'masculino','area_':'sistema','rol_':'gerente','salario_':'10000','numeroseguro_':'9898989898989','correoelectronico_':'ale@gmail.com','clave_':'12345678','numerotelefono_':'0005556767'}

        #print(valores[0])
        #print(type(valores[0]))
        
        print(type(valores))

        #valores[0]=['3232323']
        
        try:
            cursor1.execute(miSQL,valores)
            print("Se crea nuevo usuario")
            miConexion.commit()
        except:
            print("No se pudo crear el nuevo usuario'")
            miConexion.rollback()
        miConexion.close()

    def ConVerNom(self):
        print("Abrir base de datos de nominas para ver")
        import mysql.connector
        miConexion=mysql.connector.connect(host='localhost', user='root',passwd='',
                database='bddrecursoshumanos')
        cursor1=miConexion.cursor()

        miSQL='SELECT id, nombre, genero, area, rol, salario, numeroseguro, correoelectronico, clave, numerotelefono FROM nominas'
        
        try:
            cursor1.execute(miSQL)
            resultado=cursor1.fetchall()
            for datos in resultado:
                print(datos)
                
                #self.lisBN.insert("",0,text=row[0], values= (row[1],row[2],row[3],row[4],
                    #row[5],row[6],row[7],row[8],row[9]))

        except:
            print("No se pudo abrir los datos de nominas")

            miConexion.rollback()

        miConexion.close()


