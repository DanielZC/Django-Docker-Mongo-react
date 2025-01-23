from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import RegisterUserSerializer
from core.db import ConnectionDB
from common.msg import Msg


@api_view(["GET"])
def db_vars(request):

    try:
        connection_db = ConnectionDB()
        ping = connection_db.db_ping()

        return Response(
            [connection_db.get_db_connection_vars(), ping], status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(e.args[0], status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method="post",
    operation_description="Crea un usuario en la aplicación.",
    responses={
        200: "Ok",
    },
    request_body=RegisterUserSerializer,
)
@api_view(["POST"])
def register_user(request):
    try:
        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.insert(serializer.data)
            return Response(Msg.HTTP_200_OK, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(e.args[0], status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method="get",
    operation_description="Obtiene una lista de usuarios creados.",
    responses={
        200: RegisterUserSerializer(many=True),
    },
)
@api_view(["GET"])
def get_user(request):

    try:
        serializer = RegisterUserSerializer()
        data = serializer.get()
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
