import csv
import json

listadealumnos=[]
listadealumnosconpromedio=[]
listaactadecierre=[]

def procesarlista():
    try:
        with open ("ListaCurso5B.csv", "r") as archivocsv:
            lecturacsv= csv.DictReader(archivocsv)
            for alumnos in lecturacsv:
                if not alumnos.values():
                    print("hay valor vacio")
                    return None
                else:
                    listadealumnos.append(alumnos)
                    print("datos cargados")
    except:
        print("Se genero un error")                
                  

def registrarestudiante():
    try:
        rut=input("ingrese el rut del estudiante")
        nombre=input("ingrese nombre del estudiante")
        nota1=float(input("ingrese la nota 1"))
        nota2=float(input("ingrese la nota 2"))
        if not rut or not nombre:
            print("print todos los datos deben de estar llenos")
        elif 1<=nota1 <=7 and 1<=nota2 <=7:
            listadealumnos.append({
                "Rut":rut,
                "Nombre":nombre,
                "Nota 1":nota1,
                "Nota 2":nota2
            })
            print("Datos correctamente ingresados")
        else:
            print("notas invalidas")
    except:
        print("debe ingresar valores validos")

def modificarnota():
    try:
        rutamod=input("ingrese el rut a modificar")
        for alumno in listadealumnos:
            if rutamod== alumno["Rut"]:
                notaamod= float(input("1-Para modificar la primera nota\n2- para modificar la segunda nota"))
                while True:
                    nuevanota=int(input("ingrese la nueva nota"))
                    if notaamod==1:
                        if 1<=nuevanota <=7 :
                            alumno["Nota 1"]= nuevanota
                            print("modificacion correcta de notas")  
                            break
                        else:
                            print("ingrese una nota correcta")    
                    elif notaamod==2:
                        if 1<=nuevanota <=7 :
                            alumno["Nota 2"]=nuevanota
                            print("modificacion correcta de notas")  
                            break
                        else:
                            print("ingrese una nota correcta")
                    else:
                        print("debes seleccionar entre nota 1 o nota 2")        
             
    except:
        print("Debe ingresar todos los datos correctamente")
         
def eliminarestudiante():
    try:
        rutaeliminar=input("ingrese el rut a eliminar")
        for alumno in listadealumnos:
            if rutaeliminar== alumno["Rut"]:
                nombreaeliminar=input(f"estas seguro de eliminar a ,{alumno["Nombre"]} , si/no").lower()
                if nombreaeliminar== "si":
                    listadealumnos.remove(alumno)
                    print("se ha eliminado correctamente")
                else:
                    print("no se ha eliminado")    
            else:
                print("el alumno no se ha encontrado")
    except:
        print("Debe ingresar todos los datos correctamente")        

def generarpromedio():
    for alumno in listadealumnos:
        promedio= (float(alumno["Nota 1"])+ float(alumno["Nota 2"]))/2
        listadealumnosconpromedio.append({
            "Rut":alumno["Rut"],
            "Nombre":alumno["Nombre"],
            "Nota 1":alumno["Nota 1"],
            "Nota 2":alumno["Nota 2"],
            "Promedio":promedio

        })            
    print("Promedios procesados con exito")

def actadecierre():
    
    for alumnos in listadealumnosconpromedio:
        if alumnos["Promedio"]< 4:
            listaactadecierre.append({
                "Rut":alumnos["Rut"],
                "Nombre":alumnos["Nombre"],
                "Nota 1":alumnos["Nota 1"],
                "Nota 2":alumnos["Nota 2"],
                "Promedio":alumnos["Promedio"],
                "Estado":"Reprobado"

        })
        else:
            listaactadecierre.append({ 
                "Rut":alumnos["Rut"],
                "Nombre":alumnos["Nombre"],
                "Nota 1":alumnos["Nota 1"],
                "Nota 2":alumnos["Nota 2"],
                "Promedio":alumnos["Promedio"],
                "Estado":"Aprobado"
                })


    with open("archivo.csv","w")as archivotxt:
        archivoo = csv.writer(archivotxt) 
        archivoo.writerows(listaactadecierre)
    print("Proceso finalizado") 


def salir():
    
    print("Muchas grascias por preferirnos vuelva pronto")
    


while True:
    menu=int(input("""
                        1.
                        Procesar lista de estudiantes.
                        2.
                        Registrar estudiante.
                        3.
                        Modificar nota.
                        4.
                        Eliminar estudiante.
                        5.
                        Generar promedio de notas.
                        6.
                        Generar acta de cierre de curso.
                        7.
                        Salir.

    """))
    if menu== 1:
        procesarlista()
    elif menu==2:
        registrarestudiante()
    elif menu==3:
        modificarnota()
    elif menu==4:
        eliminarestudiante()
    elif menu==5:
        generarpromedio()
    elif menu==6:
        actadecierre()
    elif menu==7:
        salir()
        break
    else: 
        print("las opciones son del 1 al 7")    
    
