from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, null=True)
    title_en = models.CharField(max_length=200, null=True)
    title_jp = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    img = models.ImageField(null=True, upload_to="pokemon_images")
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="next_evolutions")

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
