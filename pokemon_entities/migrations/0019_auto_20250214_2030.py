# Generated by Django 3.1.14 on 2025-02-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0018_auto_20250214_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на английском:'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на японском:'),
        ),
    ]
