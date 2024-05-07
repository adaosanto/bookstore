from rest_framework.generics import CreateAPIView, UpdateAPIView

from .serializers import UserModelSerializer


class UserCreateView(CreateAPIView):
    permission_classes = ()
    serializer_class = UserModelSerializer


class UserUpdateView(UpdateAPIView):
    serializer_class = UserModelSerializer

    def get_object(self):
        return self.request.user
