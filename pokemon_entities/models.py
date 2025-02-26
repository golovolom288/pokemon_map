from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, default="", verbose_name="Название покемона:")
    title_en = models.CharField(max_length=200, default="", blank=True, verbose_name="Название на английском:")
    title_jp = models.CharField(max_length=200, default="", blank=True, verbose_name="Название на японском:")
    description = models.TextField(verbose_name="Описание покемона:", default="")
    img = models.ImageField(null=True, blank=True, upload_to="pokemon_images", verbose_name="Картинка покемона:")
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Предыдущая эволюция:", null=True, blank=True, related_name="next_evolutions")

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Вид покемона:",
                                related_name="Entities")
    lat = models.FloatField(verbose_name="Широта:")
    lon = models.FloatField(verbose_name="Долгота:")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Появится в:")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Пропадёт в:")
    level = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name="Уровень покемона:")
    health = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name="Здоровье покемона:")
    strength = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name="Сила покемона:")
    defence = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name="Защита покемона:")
    stamina = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name="Выносливость покемона:")

    def __str__(self):
        return '{}'.format(self.pokemon)
