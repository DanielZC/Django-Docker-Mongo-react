from rest_framework import serializers
from core.db import ConnectionDB
from common.crypt import Password


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
            raise serializers.ValidationError(
                "Este correo electronico ya ha sido registrado"
            )
        return value

    def validate_contraseña(self, value):

        crypt = Password()
        pws = crypt.encrypt_pws(value)
        return pws

    def insert(self, data):

        try:
            db_operations = ConnectionDB()
            operation = db_operations.insert_one("usuarios", data)
            return operation
        except ConnectionError as e:
            raise serializers.ValidationError(e.args[0])

    def get(self):

        try:
            db_operations = ConnectionDB()
            result = db_operations.find("usuarios")
            return result
        except ConnectionError as e:
            raise serializers.ValidationError(e.args[0])
