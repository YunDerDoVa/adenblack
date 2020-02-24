from django.contrib import admin

from .models import Movie, ArtMapping, ArtCompositing, Person
# Register your models here.
admin.site.register(Movie)
admin.site.register(ArtMapping)
admin.site.register(ArtCompositing)
admin.site.register(Person)
