# Generated by Django 4.2.7 on 2023-11-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodification_engine_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodification',
            name='engine_volume',
            field=models.PositiveIntegerField(verbose_name='Обьем двигателя'),
        ),
    ]
