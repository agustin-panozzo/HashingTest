from constantes import *
from gestion_usuario import *
from usuario import Usuario

def mostrar_menu() -> None:
    print(BIENVENIDA)
    for i in range(len(MENU)):
        print(f"{i + 1}. {MENU[i]}")

def ejecutar_menu(usuarios: list) -> None:
    mostrar_menu()
    opcion: int = int(input("Opción: "))

    while opcion != 3:

        if opcion == 1:
            usuario: Usuario = generar_usuario()
            usuarios.append(usuario)

        if opcion == 2:
            iniciar_sesion(usuarios)

        mostrar_menu()
        opcion: int = int(input("Opción: "))