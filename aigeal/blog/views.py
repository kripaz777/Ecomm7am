from django.shortcuts import render
from .models import *

from home.views import *
# Create your views here.
class BlogView(BaseView):
	def get(self,request):
		self.views['blogs'] = Blog.objects.all()
		return render(request,'blog.html',self.views)

class BlogDetailsView(BaseView):
	def get(self,request,slug):
		self.views['blogdetails'] = Blog.objects.filter(slug = slug)
		self.views['recent_blog'] = Blog.objects.all().reverse()
		return render(request,'blog-details.html',self.views)