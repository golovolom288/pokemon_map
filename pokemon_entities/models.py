from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="Название покемона:")
    title_en = models.CharField(max_length=200, null=True, verbose_name="Название на английском:")
    title_jp = models.CharField(max_length=200, null=True, verbose_name="Название на японском:")
    description = models.TextField(null=True, verbose_name="Описание покемона:")
    img = models.ImageField(null=True, upload_to="pokemon_images", verbose_name="Картинка покемона:")
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Предыдущая эволюция:", null=True, blank=True, related_name="next_evolutions")

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Вид покемона:",
                                related_name="PokemonEntities")
    Lat = models.FloatField(verbose_name="Широта:")
    Lon = models.FloatField(verbose_name="Долгота:")
    Appeared_at = models.DateTimeField(null=True, verbose_name="Появится в:")
    Disappeared_at = models.DateTimeField(null=True, verbose_name="Пропадёт в:")
    Level = models.IntegerField(null=True, verbose_name="Уровень покемона:")
    Health = models.IntegerField(null=True, verbose_name="Здоровье покемона:")
    Strength = models.IntegerField(null=True, verbose_name="Сила покемона:")
    Defence = models.IntegerField(null=True, verbose_name="Защита покемона:")
    Stamina = models.IntegerField(null=True, verbose_name="Выносливость покемона:")

    def __str__(self):
        return '{}'.format(self.pokemon)
