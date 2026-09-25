from paciente import Paciente
pacientes:list[Paciente] = [
    Paciente(rut="11.111.111-1", nombre="Luis Arriagada", edad=40, prevision="Fonasa"),
    Paciente(rut="22.222.222-2", nombre="Juan Perez", edad=30, prevision="Isapre"),
    ]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            num:int = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def menu()->int:
    print("Menu clínica")
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Imprimir un paciente")
    print("5.- Imprimir todos los pacientes")
    print("0.- Salir")
    opcion:int = leer_numero("Ingrese una opción: ")
    return opcion

def main()->None:
    while True:
        op=menu()
        if op==1:
            print("Agregando paciente...")
        elif op==2:
            print("Editando paciente...")
        elif op==3:
            print("Eliminando paciente...")
        elif op==4:
            print("Imprimiendo un paciente...")
        elif op==5:
            print("Imprimiendo todos los pacientes...")
        elif op==0:
            print("Finalizando programa...")
            break

if __name__ == "__main__":
    main()