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
    pokemons = PokemonEntity.objects.filter(id=pokemon_id)
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            pokemon_url = request.build_absolute_uri(MEDIA_URL+str(requested_pokemon.pokemon.img))
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    add_pokemon(
        folium_map, requested_pokemon.Lat,
        requested_pokemon.Lon,
        pokemon_url
    )
    page_pokemon = {
        "pokemon_id": pokemon.id,
        "img_url": pokemon_url,
        "title_ru": requested_pokemon.pokemon.title,
        "title_en": requested_pokemon.pokemon.title_en,
        "title_jp": requested_pokemon.pokemon.title_jp,
        "description": requested_pokemon.pokemon.description,
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': page_pokemon,
    })

