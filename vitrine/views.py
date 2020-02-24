from django.shortcuts import render, redirect
from django.urls import reverse

from datetime import date
from .models import Movie, ArtMapping, ArtCompositing, Person

def get_sql(request):
    return redirect('/media/db.sqlite3')


def home(request):

    context = {
        'today': date.today(),
        'plug_video_url': 'plug/aden_intro.mp4',
        'mad_mirror': 'mad_mirror',
    }

    return render(request, 'vitrine/pages/home.html.django', context)

def movie(request, code):

    previous = reverse('home')

    movie = Movie.objects.get(code=code)

    context = {
        'today': date.today(),
        'btn_return_color': 'aden-btn-gold-rose aden-btn-opacity-small-full',
        'btn_return_path': previous,
        'movie': movie,
    }

    return render(request, 'vitrine/pages/watch_movie.html.django', context)

def vfx(request):

    previous = reverse('home')

    context = {
        'today': date.today(),
        'btn_return_color': 'aden-btn-gold-rose',
        'btn_return_path': previous,
    }

    return render(request, 'vitrine/pages/vfx.html.django', context)

def art_mapping(request):

    previous = reverse('vfx')

    context = {
        'today': date.today(),
        'btn_return_color': 'aden-btn-cyan-gold',
        'btn_return_path': previous,
        'mappings': ArtMapping.objects.all(),
    }

    return render(request, 'vitrine/pages/art_mapping.html.django', context)

def art_compositing(request):

    previous = reverse('vfx')

    context = {
        'today': date.today(),
        'btn_return_color': 'aden-btn-cyan-gold',
        'btn_return_path': previous,
        'mappings': ArtCompositing.objects.all(),
    }

    return render(request, 'vitrine/pages/art_compositing.html.django', context)

def courses(request):

    previous = reverse('home')

    context = {
        'today': date.today(),
        'plug_video_url': 'plug/the_last_plug.mp4',
        'btn_return_color': 'aden-btn-white-indigo',
        'btn_return_path': previous,
    }

    return render(request, 'vitrine/pages/courses.html.django', context)

def participate_futur_project(request):

    previous = reverse('home')

    context = {
        'today': date.today(),
        'plug_video_url': 'plug/participate_futur_project.mp4',
        'btn_return_color': 'aden-btn-white-indigo',
        'btn_return_path': previous,
    }

    return render(request, 'vitrine/pages/participate_futur_project.html.django', context)

def team_contact(request):

    previous = reverse('home')

    persons = Person.objects.filter(team_contact=True)
    movies = Movie.objects.all()

    context = {
        'today': date.today(),
        'plug_video_url': 'plug/lets_get_in_touch.mp4',
        'btn_return_color': 'aden-btn-cyan-green',
        'btn_return_path': previous,
        'persons': persons,
        'movies': movies,
    }

    return render(request, 'vitrine/pages/team_contact.html.django', context)

def movie_details(request, code):

    previous = reverse('team_contact')

    movie = Movie.objects.get(code=code)
    persons = [
        movie.director,
        movie.composer,
        movie.camera_operator,
    ]

    context = {
        'today': date.today(),
        'plug_video_url': 'plug/lets_get_in_touch.mp4',
        'btn_return_color': 'aden-btn-cyan-green',
        'btn_return_path': previous,
        'movie': movie,
        'persons': persons,
    }

    return render(request, 'vitrine/pages/movie_details.html.django', context)
