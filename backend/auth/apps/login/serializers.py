from rest_framework import serializers
from core.db import ConnectionDB


class LoginSerializer(serializers.Serializer):

    correo_electronico = serializers.CharField()
    contraseña = serializers.CharField()
    hora_fecha = serializers.DateTimeField()
    ip = serializers.CharField()

    def validate(self, attrs):

        db_operations = ConnectionDB()
        result = db_operations.find_one(
            "login", {"correo_electronico": attrs["correo_electronico"]}
        )

        print(result)
        return True

    def login(self, data):

        try:
            db_operations = ConnectionDB()
            db_operations.insert_one("login", data)

            return True

        except ConnectionError as e:
            raise ValueError(str(e))
