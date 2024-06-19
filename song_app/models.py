from django.db import models

# Create your models here.
class song(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=100, blank=True, null=True)
    # genre = models.CharField(max_length=50, blank=True, null=True)
    file = models.FileField(upload_to='songs/')
    

    def __str__(self):
        return self.title