# Generated by Django 3.1.14 on 2025-01-31 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20250131_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='PokemonEntities', to='pokemon_entities.pokemon', verbose_name='pokemon'),
            preserve_default=False,
        ),
    ]
