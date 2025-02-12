import folium
import json
from pokemon_entities.models import PokemonEntity, Pokemon
from django.http import HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from pogomap.settings import MEDIA_URL



MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = timezone.localtime(timezone.now())
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(Appeared_at__lte=current_time, Disappeared_at__gte=current_time)
    for pokemon_entity in pokemon_entities:
        pokemon_url = request.build_absolute_uri(pokemon_entity.pokemon.img.url)
        add_pokemon(
            folium_map, pokemon_entity.Lat,
            pokemon_entity.Lon,
            pokemon_url
        )


    pokemons_on_page = []
    for pokemon_entity in pokemon_entities:
        pokemon_url = request.build_absolute_uri(pokemon_entity.pokemon.img.url)
        pokemons_on_page.append({
            'pokemon_id': pokemon_entity.id,
            'img_url': pokemon_url,
            'title_ru': pokemon_entity.pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemonentity = PokemonEntity.objects.get(id=pokemon_id)
        pokemon_url = request.build_absolute_uri(MEDIA_URL + str(pokemonentity.pokemon.img))
    except PokemonEntity.DoesNotExist:
        return HttpResponseNotFound("<h1>Покемон не найден<h2>")
    previous_evolution = None
    next_evolution = None
    evolution = pokemonentity.pokemon.previous_evolution
    if evolution:
        evolution_url = request.build_absolute_uri(MEDIA_URL + str(evolution.img))
        print(evolution)
        previous_evolution = {
            "pokemon_id": evolution.id,
            "img_url": evolution_url,
            "title_ru": evolution.title,
        }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    add_pokemon(
        folium_map, pokemonentity.Lat,
        pokemonentity.Lon,
        pokemon_url
    )
    page_pokemon = {
        "pokemon_id": pokemonentity.id,
        "img_url": pokemon_url,
        "title_ru": pokemonentity.pokemon.title,
        "title_en": pokemonentity.pokemon.title_en,
        "title_jp": pokemonentity.pokemon.title_jp,
        "description": pokemonentity.pokemon.description,
        "previous_evolution": previous_evolution
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': page_pokemon,
    })

