from django.shortcuts import render
from django.views.generic import View
from .models import *
from company.models import *
# Create your views here.
class BaseView(View):
	views = {}
	views['logos'] = Logo.objects.all()
	views['products'] = Product.objects.all()

class HomeView(BaseView):
	def get(self,request):
		self.views['sliders'] = Slider.objects.all()
		self.views['offerings'] = Offering.objects.all()
		self.views['projects'] = Project.objects.all()
		self.views['testinomials'] = Testimonial.objects.all()
		self.views['Partners'] = Partner.objects.all()
		return render(request,'index.html',self.views)