from django.db import models
from .choices import LEVELS_CHOICES, STATUS_CHOICES


class MoUser(models.Model):  # пользователи
    email = models.CharField(max_length=100, unique=True, verbose_name='почта')
    phone = models.IntegerField(unique=True, verbose_name='Телефон')
    fam = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    otc = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'


class Coords(models.Model):  # координаты
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f"широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}"


class Level(models.Model):  # уровень сложность
    winter = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Зима')
    summer = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Лето')
    autumn = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Осень')
    spring = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Весна')

    def __str__(self):
        return f"зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}"


class Mountpass(models.Model):  # Перевал
    beautyTitle = models.CharField(default='пер.', max_length=255, verbose_name='краткое название')
    title = models.CharField(blank=True, null=True, max_length=255, verbose_name='название')
    other_titles = models.CharField(blank=True, null=True, max_length=255, verbose_name='Другое название')
    connect = models.CharField(max_length=255, blank=True, null=True, verbose_name='Что связывает')
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MoUser, on_delete=models.CASCADE, default=None, verbose_name='Турист')
    coord = models.OneToOneField(Coords, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Координаты')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NW', verbose_name='Статус')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Уровень сложности')

    def __str__(self):
        return f'{self.pk} {self.beautyTitle}'


def get_path_upload_images(instance, file):
    return f'images/mount-{instance.mount.id}/{file}'


class Images(models.Model):  # фото местности
    mount = models.ForeignKey(Mountpass, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to=get_path_upload_images, blank=True, null=True, verbose_name='Изображение')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')

    def __str__(self):
        return f'{self.mount}'


