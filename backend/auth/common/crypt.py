import bcrypt


class Password:
    def encrypt_pws(self, pws):
        """
        Encripta una contraseña utilizando bcrypt.

        Args:
            password (str): La contraseña en texto plano a encriptar.

        Returns:
            str: La contraseña encriptada.
        """

        # Convertir la contraseña a bytes
        password_bytes = pws.encode("utf-8")
        # Generar el salt
        salt = bcrypt.gensalt()
        # Generar el hash
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        # Retornar la contraseña encriptada como string
        return hashed_password.decode("utf-8")

    def validate_pws(self, pws, pws_hash):
        """
        Verifica si una contraseña coincide con su hash encriptado.

        Args:
            password (str): La contraseña en texto plano a verificar.
            hashed_password (str): La contraseña encriptada para comparar.

        Returns:
            bool: True si coincide, False de lo contrario.
        """

        # Convertir la contraseña y el hash a bytes
        password_bytes = pws.encode("utf-8")
        hashed_password_bytes = pws_hash.encode("utf-8")
        # Verificar la contraseña
        return bcrypt.checkpw(password_bytes, hashed_password_bytes)
