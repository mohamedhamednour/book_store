from rest_framework import mixins, viewsets


from .serializers import (
    LoginSerializer,
    UserSerializer,
)
from .models import User
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        return super().get_serializer_class()

    @action(methods=["post"], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
