from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer


# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer