from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(default = 'demo',max_length = 200)
    video = models.FileField(upload_to = 'video')
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name