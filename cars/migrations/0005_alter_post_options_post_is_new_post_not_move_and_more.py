# Generated by Django 4.2.7 on 2023-11-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_carmodification_engine_volume'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьвления'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='Новая'),
        ),
        migrations.AddField(
            model_name='post',
            name='not_move',
            field=models.BooleanField(default=False, verbose_name='Не на ходу'),
        ),
        migrations.AddField(
            model_name='post',
            name='to_order',
            field=models.BooleanField(default=False, verbose_name='На заказ'),
        ),
    ]
