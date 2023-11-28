
import pickle
import alumno as alu

listaAlumnos=None
fileAlumnos = "alumnos.pkl"

def cargarAlumnos(file):
    try:
        with open(file,'rb') as f:
            alumnos_datos = pickle.load(f)
            return alumnos_datos
    except FileNotFoundError:
        return []

def refreshAlumnoDatos():
    global listaAlumnos
    listaAlumnos= cargarAlumnos(fileAlumnos)

def listarAlumnos(listaAlumnos):
    print('---------------------------------------------------')
    print('Nombre\t\tApellidos\tEdad\tNota\tNacionalidad')
    print('---------------------------------------------------')
    for alu in listaAlumnos:        
        print(f'{alu.Nombre}\t{alu.Apellido}\t\t{alu.Edad}\t{alu.Nota}\t{alu.Nacionalidad}')
    print('---------------------------------------------------')        
        
def registrarAlumno(listaAlumnos, file):
    print("*****Registro de Alumno*****")
    Nombre       = input("->Nombre      : ")
    Apellido     = input("->Apellido    : ")
    Edad         = input("->Edad        : ")
    Nacionalidad = input("->Nacionalidad: ")
    alumno = alu.alumno(Nombre, Apellido,Edad,Nacionalidad)
    listaAlumnos.append(alumno)
    
    guardarAlumno(listaAlumnos, file)

def guardarAlumno(listaAlumnos, file):
    with open(file,'wb') as f:
         pickle.dump(listaAlumnos,f)
         print("Alumno Registrado")

def calificarAlumnos(listaAlumnos,file):    
    if len(listaAlumnos)>0:
        for alu in listaAlumnos:
            while True:
                dato = input(f'Alumno {alu.Nombre} {alu.Apellido}, Ingrese nota: ')
                try:
                    nota = int(dato)
                except ValueError:
                    nota = -1
                
                if 0<=nota<=20:
                    alu.setNota(nota)                
                    break
        guardarAlumno(listaAlumnos, file)        
    else:
        print("No hay alumnos con notas registradas")    

def obtenerPromedio(listaAlumnos):
    if len(listaAlumnos)>0:
        suma = 0
        cant = 0
        for alu in listaAlumnos:
            if alu.Nota is not None:
                suma = suma + alu.Nota
                cant = cant + 1
        if suma>0:        
            promedio = suma/cant
            print(f"El promedio de notas para {cant} alumno(s) es: {promedio}")
            print(f"El valor del promedio se obtuvo de los alumnos poseen notas registradas")
        else:
            print("No hay alumnos con notas registradas")    
    else:
        print("No hay alumnos con notas registradas")

def obtenerSumaNotas(listaAlumnos):
    if len(listaAlumnos)>0:
        suma = 0
        cant = 0
        for alu in listaAlumnos:
            if alu.Nota is not None:
                suma = suma + alu.Nota
                cant = cant + 1
        if suma>0:   
            print(f"La suma de notas para {cant} alumno(s) es: {suma}")
            print(f"El valor de la suma se obtuvo de los alumnos poseen notas registradas")
        else:
            print("No hay alumnos con notas registradas")    
    else:
        print("No hay alumnos con notas registradas")
            
while True:
    print('=================================================')
    print('-------> BIENVENIDO AL REGISTRO DE NOTAS <-------')
    print('=================================================')
    print('\tR: Registrar Alumno.......')
    print('\tL: Listar Alumnos.........')
    print('\tC: Calificar Alumno.......')
    print('\tP: Obtener Promedio.......')
    print('\tS: Desplegar Suma de Notas')
    print('\tX: Finalizar aplicacion...')
    print('=================================================')
    opc = input("Ingrese Comando: ").upper()
                       
    if opc not in ('RLCPSX'):
        print('Comando Invalido')
    else:
        refreshAlumnoDatos()        
        if opc == 'R':            
            registrarAlumno(listaAlumnos, fileAlumnos)
        elif opc == 'L':                 
            listarAlumnos(listaAlumnos)   
        elif opc == 'C':                    
            calificarAlumnos(listaAlumnos,fileAlumnos) 
        elif opc == 'P':            
            obtenerPromedio(listaAlumnos)
        elif opc == "S":            
            obtenerSumaNotas(listaAlumnos)    
        elif opc == 'X':
            print('Programa finalizado')
            break
            
    
