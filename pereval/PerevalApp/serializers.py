from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from rest_framework import serializers


class MoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoUser
        fields = [
            'name',
            'email',
            'phone',
            'fam',
            'name',
            'otc',
        ]
        verbose_name = 'Турист'


class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height'
        ]
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = [
            'winter',
            'summer',
            'autumn',
            'spring'
        ]
        verbose_name = 'Уровень сложности'


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.URLField()

    class Meta:
        model = Images
        fields = [
            'image',
            'title',
        ]
        verbose_name = 'Фото'


class MountpassSerializer(WritableNestedModelSerializer):
    user = MoUserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Mountpass
        fields = [
            'id',
            'beautyTitle',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user',
            'coords',
            'level',
            'images',
            'status',
        ]
        read_only_fields = ['status']





