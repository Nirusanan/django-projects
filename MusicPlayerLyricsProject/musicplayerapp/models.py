from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.TextField ()
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=100, blank=True, null=True)
    lyrics = models.TextField(blank=True,null=True)
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title