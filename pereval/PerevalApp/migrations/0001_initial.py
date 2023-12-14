# Generated by Django 4.1.3 on 2023-12-14 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б')], max_length=6, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б')], max_length=6, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б')], max_length=6, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б')], max_length=6, null=True, verbose_name='Весна')),
            ],
        ),
        migrations.CreateModel(
            name='MoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='почта')),
                ('phone', models.IntegerField(unique=True, verbose_name='Телефон')),
                ('fam', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('otc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Mountpass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beautyTitle', models.CharField(default='пер.', max_length=255, verbose_name='красивое название')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='название')),
                ('other_titles', models.CharField(blank=True, max_length=255, null=True, verbose_name='Другое название')),
                ('connect', models.CharField(blank=True, max_length=255, null=True, verbose_name='Что связывает')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NW', 'Новый'), ('AC', 'На модерации'), ('PN', 'Принят'), ('RJ', 'Отклонён')], default='NW', max_length=2, verbose_name='Статус')),
                ('coord', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PerevalApp.coords', verbose_name='Координаты')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PerevalApp.level', verbose_name='Уровень сложности')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='PerevalApp.mouser', verbose_name='Турист')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(null=True, verbose_name='Ссылка на изображение')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('mount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='PerevalApp.mountpass')),
            ],
        ),
    ]