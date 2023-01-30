from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from .models import User
from .serializers import UserSerializer
from rest_framework import generics

class UserAPIView(generics.ListAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = (IsAdminUser,)
   def permission_denied(self, request, message=None, code=None):
      raise PermissionDenied("You are not an admin")

