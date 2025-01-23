from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LoginSerializer
from common.msg import Msg


@api_view(["POST"])
def login(request):

    try:
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.login(serializer.data)
            return Response(Msg.HTTP_200_OK, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
