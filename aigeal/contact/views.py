from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from home.views import *
from django.contrib import messages
# Create your views here.

class ContactView(BaseView):
    def get(self,request):

        return render(request,'contact.html')

def contacts(request):

    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message =message,
            
        )
        data.save()
        messages.success(request, 'Message sent. Thank You')
        return redirect('/contact/')

    return redirect('/contact/')