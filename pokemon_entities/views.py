import folium
import json
from pokemon_entities.models import PokemonEntity, Pokemon
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
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
    pokemon_entities = PokemonEntity.objects.filter(appeared_at__lte=current_time, disappeared_at__gte=current_time)
    for pokemon_entity in pokemon_entities:
        pokemon_url = request.build_absolute_uri(pokemon_entity.pokemon.img.url)
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
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
    pokemonentity = get_object_or_404(PokemonEntity, id=pokemon_id)
    pokemon_url = request.build_absolute_uri(MEDIA_URL + str(pokemonentity.pokemon.img))
    prev_evolution_data = None
    n_evolution_data = None
    next_evolution = pokemonentity.pokemon.next_evolutions.first()
    previous_evolution = pokemonentity.pokemon.previous_evolution
    if previous_evolution:
        evolution_url = request.build_absolute_uri(MEDIA_URL + str(previous_evolution.img))
        prev_evolution_data = {
            "pokemon_id": previous_evolution.id,
            "img_url": evolution_url,
            "title_ru": previous_evolution.title,
        }
    if next_evolution:
        evolution_url = request.build_absolute_uri(MEDIA_URL + str(next_evolution.img))
        n_evolution_data = {
            "pokemon_id": next_evolution.id,
            "img_url": evolution_url,
            "title_ru": next_evolution.title,
        }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    add_pokemon(
        folium_map, pokemonentity.lat,
        pokemonentity.lon,
        pokemon_url
    )
    page_pokemon = {
        "pokemon_id": pokemonentity.id,
        "img_url": pokemon_url,
        "title_ru": pokemonentity.pokemon.title,
        "title_en": pokemonentity.pokemon.title_en,
        "title_jp": pokemonentity.pokemon.title_jp,
        "description": pokemonentity.pokemon.description,
        "previous_evolution": prev_evolution_data,
        "next_evolution": n_evolution_data
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': page_pokemon,
    })

