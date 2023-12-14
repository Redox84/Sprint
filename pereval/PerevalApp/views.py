
import django_filters.rest_framework
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = MoUser.objects.all()
    serializer_class = MoUserSerializer
    filterset_fields = ['fam', 'name', 'otc', 'email']


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = LevelSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class MountpassViewSet(viewsets.ModelViewSet):
    queryset = Mountpass.objects.all()
    serializer_class = MountpassSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    # Создаем перевал
    def create(self, request, *args, **kwargs):
        serializer = MountpassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Успешно!',
                    'id': serializer.data['id'],
                }
            )
        if status.HTTP_400_BAD_REQUEST:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Некорректный запрос серверу',
                    'id': None,
                }
            )
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Ошибка сервера',
                    'id': None,
                }
            )

