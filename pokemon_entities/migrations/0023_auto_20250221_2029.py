# Generated by Django 3.1.14 on 2025-02-21 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0022_auto_20250221_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Appeared_at',
            new_name='appeared_at',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Defence',
            new_name='defence',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Disappeared_at',
            new_name='disappeared_at',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Health',
            new_name='health',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lon',
            new_name='lon',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Stamina',
            new_name='stamina',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Strength',
            new_name='strength',
        ),
    ]
