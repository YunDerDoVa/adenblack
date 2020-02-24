from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vfx/', views.vfx, name='vfx'),
    path('vfx/mapping', views.art_mapping, name='art_mapping'),
    path('vfx/compositing', views.art_compositing, name='art_compositing'),
    path('courses/', views.courses, name='courses'),
    path('participate_futur_project/', views.participate_futur_project, name='participate_futur_project'),
    path('team_contact/', views.team_contact, name='team_contact'),
    path('movie/<str:code>/', views.movie, name='movie'),
    path('movie_details/<str:code>/', views.movie_details, name='movie_details'),
]
