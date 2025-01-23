import bcrypt


class Password:
    def encrypt_pws(self, pws):
        # Generar un salt y hashear la contraseña
        salt = bcrypt.gensalt()
        pws_hash = bcrypt.hashpw(pws.encode("utf-8"), salt)
        return pws_hash

    # Función para verificar una contraseña
    def validate_pws(self, pws, pws_hash):
        # Verificar si la contraseña coincide con el hash almacenado
        return bcrypt.checkpw(pws.encode("utf-8"), pws_hash)
