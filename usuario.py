import bcrypt

class Usuario:  
    def __init__(self, nombre: str, clave: str) -> None:
        self.nombre = nombre
        self.salt = bcrypt.gensalt()
        self.clave_hash = self.hash_clave(clave)
        
    def hash_clave(self, clave: str) -> str:
        clave_bytes = clave.encode('utf-8')
        clave_hash = bcrypt.hashpw(clave_bytes, self.salt)
        return clave_hash
    
    def verificar_clave(self, clave: str) -> bool:
        clave_bytes = clave.encode('utf-8')
        return bcrypt.checkpw(clave_bytes, self.clave_hash)