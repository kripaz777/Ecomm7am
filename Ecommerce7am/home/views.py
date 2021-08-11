from django.shortcuts import render
from .models import *
from django.views import View

# Create your views here.
class BaseView(View):
	views = {}
	views['categories'] = Category.objects.all()
	views['subcategories'] = SubCategory.objects.all()


class HomeView(BaseView):
	def get(self,request):
		self.views['sliders'] = Slider.objects.all()
		# self.views['categories'] = Category.objects.all()
		self.views['items'] = Item.objects.filter(status = 'Active')
		self.views['brands'] = Brand.objects.all()
		self.views['ads'] = Ad.objects.all()
		return render(request,'index.html',self.views)