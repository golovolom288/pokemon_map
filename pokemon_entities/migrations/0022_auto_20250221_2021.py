# Generated by Django 3.1.14 on 2025-02-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0021_auto_20250221_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='Defence',
            field=models.FloatField(null=True, verbose_name='Защита покемона:'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Health',
            field=models.FloatField(null=True, verbose_name='Здоровье покемона:'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Level',
            field=models.FloatField(null=True, verbose_name='Уровень покемона:'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.FloatField(null=True, verbose_name='Выносливость покемона:'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Strength',
            field=models.FloatField(null=True, verbose_name='Сила покемона:'),
        ),
    ]
