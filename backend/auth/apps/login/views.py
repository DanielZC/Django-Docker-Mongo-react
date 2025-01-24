from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from .serializers import LoginSerializer
from common.msg import Msg


@swagger_auto_schema(
    method="post",
    operation_description="Loguea a un usuario.",
    responses={
        200: "Ok",
    },
    request_body=LoginSerializer,
)
@api_view(["POST"])
def login(request):

    try:
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.login(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
