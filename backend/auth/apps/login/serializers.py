from rest_framework import serializers

from core.db import ConnectionDB
from common.crypt import Password


class LoginSerializer(serializers.Serializer):

    correo_electronico = serializers.CharField()
    contraseña = serializers.CharField(write_only=True)
    nombre = serializers.CharField(read_only=True)
    hora_fecha = serializers.DateTimeField(required=False)
    ip = serializers.CharField(required=False)

    def validate_pws(self, pws, pws_hash):

        crypt = Password()
        return crypt.validate_pws(pws, pws_hash)

    def validate(self, attrs):

        db_operations = ConnectionDB()
        result = db_operations.find_one(
            "usuarios", {"correo_electronico": attrs["correo_electronico"]}
        )

        if result:
            pws = self.validate_pws(attrs["contraseña"], result["contraseña"])
            if pws:
                return {
                    "nombre": result["nombre"],
                    "correo_electronico": result["correo_electronico"],
                }
        raise serializers.ValidationError("Usuario y/o contraseña incorrecta")

    def login(self, data):

        try:
            db_operations = ConnectionDB()
            db_operations.insert_one("login", data)

            return True

        except ConnectionError as e:
            raise serializers.ValidationError(str(e))
