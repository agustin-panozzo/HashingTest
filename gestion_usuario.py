from usuario import Usuario

def generar_usuario() -> Usuario:
    nombre: str = input('Ingrese nombre de usuario: ')
    clave: str = input('Ingrese clave: ')
    usuario_nuevo: Usuario = Usuario(nombre, clave)

    return usuario_nuevo

def iniciar_sesion(usuarios: list) -> None:
    nombre: str = input("Ingrese nombre de usuario: ")
    clave: str = input("Ingrese clave: ")

    for usuario in usuarios:
        if (usuario.nombre == nombre and usuario.verificar_clave(clave)):
            print("Sesión iniciada con éxito")

        else:
            print("Nombre de usuario o clave incorrectos")