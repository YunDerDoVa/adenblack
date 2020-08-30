from django.db import models

# Create your models here.
class Video(models.Model):

    name = models.CharField(max_length=63)
    casting = models.ManyToManyField('Person', blank=True)
    code = models.CharField(max_length=63, unique=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    poster = models.ImageField(upload_to='video/posters/', null=True, blank=True)

    class Meta:
        abstract = True

    def get_poster_url(self):
        if self.poster:
            return self.poster.url
        else:
            return None

class Movie(Video):

    director = models.ForeignKey(
        'Person',
        on_delete=models.SET_NULL,
        null=True,
        related_name='directors',
        related_query_name='directors',
    )
    composer = models.ForeignKey(
        'Person',
        on_delete=models.SET_NULL,
        null=True,
        related_name='composers',
        related_query_name='composers',
    )
    camera_operator = models.ForeignKey(
        'Person',
        on_delete=models.SET_NULL,
        null=True,
        related_name='camera_operators',
        related_query_name='camera_operators',
    )

    def __str__(self):
        return self.name

class ArtMapping(Video):

    owner = models.ForeignKey(
        'Person',
        on_delete=models.SET_NULL,
        null=True,
        related_name='owned_mappings',
        related_query_name='owned_mappings',
    )

    def __str__(self):
        return self.name

class ArtCompositing(Video):

    owner = models.ForeignKey(
        'Person',
        on_delete=models.SET_NULL,
        null=True,
        related_name='owned_compositings',
        related_query_name='owned_compositings',
    )

    def __str__(self):
        return self.name

class Person(models.Model):
    firstname = models.CharField(max_length=63)
    lastname = models.CharField(max_length=63)
    team_contact = models.BooleanField(default=False)
    job = models.CharField(max_length=63, null=True, blank=True)
    pseudo = models.CharField(max_length=63, null=True, blank=True)
    phone = models.CharField(max_length=63, null=True, blank=True)
    insta = models.CharField(max_length=63, null=True, blank=True)
    facebook = models.CharField(max_length=63, null=True, blank=True)
    soundcloud = models.CharField(max_length=63, null=True, blank=True)
    youtube = models.CharField(max_length=63, null=True, blank=True)

    def __str__(self):
        return self.pseudo + ' (' + self.firstname + ' ' + self.lastname + ')'
