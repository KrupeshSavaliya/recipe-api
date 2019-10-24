from  rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create a user"""
    serializer_class = UserSerializer