from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 500)
	email = models.EmailField(max_length = 500)
	subject = models.TextField(max_length = 500,blank = True)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name