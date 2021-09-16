from django.shortcuts import render
from .models import *
from home.views import *
# Create your views here.


class About(BaseView):
	def get(self,request):
		self.views['teams'] = Team.objects.all()
		return render(request,'about.html',self.views)

class Carrer(BaseView):
	def get(self,request):
		self.views['careeries'] = Career.objects.all()
		return render(request,'career.html',self.views)

class CarrerDetails(BaseView):
	def get(self,request,slug):
		self.views['view_careeries'] = Career.objects.filter(slug = slug)
		return render(request,'job-apply.html',self.views)

class Solutions(BaseView):
	def get(self,request):
		self.views['solutions'] = Solution.objects.all()
		return render(request,'solutions.html',self.views)

class ProjectDetail(BaseView):
	def get(self,request,slug):
		self.views['projects'] = Project.objects.filter(slug=slug)
		return render(request,'project-details.html',self.views)

class ProductDetail(BaseView):
	def get(self,request,slug):
		self.views['products'] = Product.objects.filter(slug=slug)
		return render(request,'product-detail.html',self.views)

