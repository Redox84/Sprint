
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from django.urls import reverse

from .serializers import MountpassSerializer


class MountpassTestCase(APITestCase):
    # Метод setUp запускается перед каждым тестовым примером
    # (для настройки объектов, которые могут изменяться во время тестов)
    def setUp(self):
        # Объекты первого перевала
        self.mount_1 = Mountpass.objects.create(
            user=MoUser.objects.create(
                email='cruzen@example.com',
                phone='89271234567',
                fam='Иван',
                name='Крузенштерн',
                otc='Федорович'
            ),
            beautyTitle='пер.',
            title='Riffltor',
            other_titles='433.Альпы',
            connect='ледн. Karlingerkees - ледн. Pasterzenboden',
            coord=Coords.objects.create(
                latitude=47.12173,
                longitude=12.68298,
                height=3100
            ),
            level=Level.objects.create(
                winter='1b',
                summer='1a',
                autumn='1a',
                spring='1a'
            )
        )
        # Изображеение первого перевала
        self.image_1 = Images.objects.create(
            image="https://w.forfun.com/fetch/5d/5d94ad27b68ed87ab6bda49e3b90f923.jpeg",
            title="title",
            mount=self.mount_1
        )

        # Объекты второго перевала
        self.mount_2 = Mountpass.objects.create(
            user=MoUser.objects.create(
                email='mail@example.com',
                phone='+79991234567',
                fam='Боб',
                name='Билли',
                otc='Торнтон'
            ),
            beautyTitle='пер.',
            title='Brizio',
            other_titles='433.Альпы',
            connect='ледн. Karlingerkees - ледн. Pasterzenboden',
            coord=Coords.objects.create(
                latitude=43.6148,
                longitude=41.10383,
                height=2892
            ),
            level=Level.objects.create(
                winter='1a',
                summer='1a',
                autumn='1a',
                spring='1a'
            )
        )
        # Изображеение второго перевала
        self.image_2 = Images.objects.create(
            image="https://w.forfun.com/fetch/a2/a25db975a53054fe0e27437a5fc43533.jpeg",
            title="title",
            mount=self.mount_2
        )

    # Проверка получения всех записей о перевале
    def test_mountpass_list(self):
        response = self.client.get(reverse('mountpass-list'))
        serializer_data = MountpassSerializer(
            [self.mount_1, self.mount_2],
            context={'request': response.wsgi_request},
            many=True
        ).data
        # Функции проверки утверждений
        # (позволяют проверять различные условия и ожидаемые результаты)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    # Проверка получение записи о первом перевале
    def test_mountpass_detail(self):
        response = self.client.get(reverse('mountpass-detail', kwargs={'pk': self.mount_1.id}))
        serializer_data = MountpassSerializer(self.mount_1, context={'request': response.wsgi_request}).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Проверяем создание записи обо всех объектах,
    # добавленных пользователем с почтой user.email
    def test_by_mail(self):
        email = self.mount_1.user.email
        url = f'/mount/?user__email={email}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MountpassSerializerTestCase(TestCase):
    def setUp(self):
        self.mount_1 = Mountpass.objects.create(
            id=2,
            beautyTitle="пер.",
            title="Riffltor",
            other_titles="433.Альпы",
            connect="ледн. Karlingerkees - ледн. Pasterzenboden",
            add_time="2023-11-24T14:33:19.590646Z",
            user=MoUser.objects.create(
                email="cruzen@example.com",
                phone="89271234567",
                fam="Иван",
                name="Крузенштерн",
                otc="Федорович"
            ),
            coord=Coords.objects.create(
                latitude=47.12173,
                longitude=12.68298,
                height=3100
            ),
            level=Level.objects.create(
                winter="1b",
                summer="1a",
                autumn="1a",
                spring="1a"
            )
        )

        self.image_1 = Images.objects.create(
            image="https://w.forfun.com/fetch/5d/5d94ad27b68ed87ab6bda49e3b90f923.jpeg",
            title="title",
            mount=self.mount_1
        )

        self.mount_2 = Mountpass.objects.create(
            id=3,
            beautyTitle="пер.",
            title="Brizio",
            other_titles="433.Альпы",
            connect="ледн. Karlingerkees - ледн. Pasterzenboden",
            add_time="2023-11-24T14:46:17.390528Z",
            user=MoUser.objects.create(
                email="mail@example.com",
                phone="+79991234567",
                fam="Боб",
                name="Билли",
                otc="Торнтон"
            ),
            coord=Coords.objects.create(
                latitude=43.6148,
                longitude=41.10383,
                height=2892
            ),
            level=Level.objects.create(
                winter="1a",
                summer="1a",
                autumn="1a",
                spring="1a"
            )
        )

        self.image_2 = Images.objects.create(
            image="https://w.forfun.com/fetch/a2/a25db975a53054fe0e27437a5fc43533.jpeg",
            title="title",
            mount=self.mount_2
        )
