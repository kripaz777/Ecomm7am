from django.db import models
from djrichtextfield.models import RichTextField
from django.urls import reverse
# Create your models here.
CATEGORY = (('Full Time','Full Time'),('Part Time','Part Time'),('Contract','Contract'),('Remote','Remote'),('Internship','Internship'))

class Offering(models.Model):
	title = models.CharField(max_length = 300)
	description = models.TextField(blank = True)
	slug = models.TextField(unique = True)
	image = models.FileField(upload_to = 'media')
	image_light = models.FileField(upload_to = 'media',null = True)
	added_date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title
class Project(models.Model):
	title = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'media')
	slug = models.CharField(unique = True,max_length = 500)
	description = RichTextField(blank = True)
	def __str__(self):
		return self.title

	def get_project_url(self):
		return reverse("company:project",kwargs={'slug':self.slug})

class Product(models.Model):
	title = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'media')
	slug = models.CharField(unique = True,max_length = 500)
	description = RichTextField(blank = True)
	def __str__(self):
		return self.title

	def get_product_url(self):
		return reverse("company:product",kwargs={'slug':self.slug})

class Solution(models.Model):
	title = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'media')
	slug = models.CharField(unique = True,max_length = 500)
	description = RichTextField(blank = True)
	def __str__(self):
		return self.title

class Team(models.Model):
	name = models.CharField(max_length = 500)
	designation = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'media')
	facebook_url = models.URLField(blank = True)
	linkedin_url = models.URLField(blank = True)
	twitter_url = models.URLField(blank = True)
	rank = models.IntegerField()

	def __str__(self):
		return self.name

class Career(models.Model):
	title = models.TextField()
	category = models.CharField(choices = CATEGORY,max_length= 200)
	image = models.ImageField(upload_to = 'media')
	slug = models.TextField(unique= True)
	location = models.CharField(max_length = 500,blank = True)
	description = RichTextField()
	url = models.URLField(default = "https://www.linkedin.com")

	def __str__(self):
		return self.title

	def get_job_url(self):
		return reverse("company:apply",kwargs={'slug':self.slug})