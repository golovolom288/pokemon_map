from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True, upload_to="pokemon_images")

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="pokemon",
                                related_name="PokemonEntities")
    Lat = models.FloatField()
    Lon = models.FloatField()
    Appeared_at = models.DateTimeField(null=True)
    Disappeared_at = models.DateTimeField(null=True)
    Level = models.IntegerField(null=True)
    Health = models.IntegerField(null=True)
    Strength = models.IntegerField(null=True)
    Defence = models.IntegerField(null=True)
    Stamina = models.IntegerField(null=True)

    def __str__(self):
        return '{}'.format(self.pokemon)
