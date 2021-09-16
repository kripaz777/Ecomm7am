from django.db import models

# Create your models here.
class Logo(models.Model):
	title = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	added_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title


class Slider(models.Model):
	title = models.TextField(blank = True)
	description = models.TextField(blank = True)
	secondary_description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField()
	added_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title



class Partner(models.Model):
	title = models.CharField(max_length = 300)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField()
	added_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title

class Testimonial(models.Model):
	name = models.CharField(max_length = 500)
	designation = models.CharField(max_length = 500)
	testimonial = models.TextField()
	image = models.ImageField(upload_to = 'media',null = True)
	def __str__(self):
		return self.name




