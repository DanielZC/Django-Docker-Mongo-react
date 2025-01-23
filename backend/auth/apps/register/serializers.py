from rest_framework import serializers
from core.db import ConnectionDB


class ClientInformationSerializer(serializers.Serializer):

    ip = serializers.CharField()


class RegisterUserSerializer(serializers.Serializer):

    nombre = serializers.CharField()
    correo_electronico = serializers.CharField()
    contraseña = serializers.CharField()
    cliente = ClientInformationSerializer(allow_null=True)

    def validate_correo_electronico(self, value):

        db_operations = ConnectionDB()
        result = db_operations.find_one("usuarios", {"correo_electronico": value})

        if result:
            raise ValueError("Este correo electronico ya ha sido registrado")
        return value

    def insert(self, data):

        try:
            db_operations = ConnectionDB()
            operation = db_operations.insert_one("usuarios", data)
            return operation
        except ConnectionError as e:
            raise ValueError(e.args[0])

    def get(self):

        try:
            db_operations = ConnectionDB()
            result = db_operations.find("usuarios")
            return result
        except ConnectionError as e:
            raise ValueError(e.args[0])
