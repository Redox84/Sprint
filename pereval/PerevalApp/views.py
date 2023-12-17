import django_filters
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from .models import *


class MoUserViewSet(viewsets.ModelViewSet):
    queryset = MoUser.objects.all()
    serializer_class = MoUserSerializer
    filterset_fields = ['fam', 'name', 'otc', 'email']


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class MountpassViewSet(viewsets.ModelViewSet):
    queryset = Mountpass.objects.all()
    serializer_class = MountpassSerializer
    # Список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
    # Вывод данных по ид
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('user__email', 'id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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

    # Возможность частичного редактирования данных о перевале (при статусе "new")
    def update(self, request, *args, **kwargs):
        mount = self.get_object()
        if mount.status == 'NW':
            serializer = MountpassSerializer(mount, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': '1',
                        'message': 'Изменения в записи внесены'
                    }
                )
            else:
                return Response(
                    {
                        'state': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message': f'Текущий статус: {mount.get_status_display()}, изменить запись нельзя!'
                }
            )
