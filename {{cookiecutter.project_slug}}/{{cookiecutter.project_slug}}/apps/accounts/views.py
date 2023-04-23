from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


@method_decorator(name="list", decorator=swagger_auto_schema(
    operation_summary='获取用户列表',
    operation_description='',
))
@method_decorator(name="create", decorator=swagger_auto_schema(
    operation_summary='创建用户',
    operation_description='',
))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
