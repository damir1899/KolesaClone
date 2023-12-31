# Generated by Django 4.2.7 on 2023-11-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Модификация')),
                ('horses_power', models.PositiveIntegerField(verbose_name='Лошадиные силы')),
                ('engine_type', models.IntegerField(choices=[(1, 'Бензин'), (2, 'Дизель'), (3, 'Газ-бензин'), (4, 'Газ'), (5, 'Гибрид'), (6, 'Электрический')], verbose_name='Тип двигателя')),
                ('engine_volume', models.PositiveIntegerField(max_length=20, verbose_name='Обьем двигателя')),
                ('transmission', models.IntegerField(choices=[(1, 'Механическая'), (2, 'Автомат'), (3, 'Типтроник'), (4, 'Вариатор'), (5, 'Робот')], verbose_name='Коробка передач')),
                ('drive_type', models.IntegerField(choices=[(1, 'Передний привод'), (2, 'Задний привод'), (3, 'Полный привод')], verbose_name='Привод')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.AddField(
            model_name='cargeneration',
            name='car_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cars.cartype', verbose_name='Кузов'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(verbose_name='Описание')),
                ('kilometrage', models.PositiveBigIntegerField(verbose_name='Пробег')),
                ('wheel', models.IntegerField(choices=[(1, 'Справа'), (2, 'Слева')], default=2, verbose_name='Расположение руля')),
                ('is_cleared', models.BooleanField(verbose_name='Растаможен')),
                ('color', models.IntegerField(choices=[(1, 'Белый'), (2, 'Зеленый'), (3, 'Черный'), (4, 'Синий'), (5, 'Оранжевый'), (6, 'Красный')], verbose_name='Цвет')),
                ('price', models.PositiveBigIntegerField(verbose_name='Цена')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_user.profileuser', verbose_name='Автор')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.carmodification', verbose_name='Модификация')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.city', verbose_name='Город')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file_name', models.TextField()),
                ('file_size', models.PositiveBigIntegerField(help_text='File size in bytes')),
                ('local_file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('s3_url', models.TextField(blank=True)),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='auth_user.profileuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='carmodification',
            name='generation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.cargeneration', verbose_name='Поколение'),
        ),
    ]
