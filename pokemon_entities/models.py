from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    Lan = models.FloatField()
    Lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="pokemon", related_name="PokemonEntities")
    Appeared_at = models.DateTimeField(null=True)
    Disappeared_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{}'.format(self.pokemon)
