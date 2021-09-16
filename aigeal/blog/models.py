from django.db import models
from djrichtextfield.models import RichTextField
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
	title = models.TextField()
	slug = models.TextField(unique = True)
	author = models.CharField(max_length = 500)
	author_image = models.ImageField(upload_to = 'media')
	description = RichTextField()
	banner = models.ImageField(upload_to = "media")
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

	def get_subcat_url(self):
		return reverse("blog:details",kwargs={'slug':self.slug})
