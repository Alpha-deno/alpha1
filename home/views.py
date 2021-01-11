from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Service,Restaurant
from django.views.generic import  ListView
from itertools import chain
from django.db.models import Q
from business.models import Businessuser
from business.models import User
from .form import ContantForm
from django.contrib import messages


def home(request, username=None):
    
    #if request.user:
    #    setbs = Businessuser.objects.filter(business=request.user)
    #else:
    #    setbs = Businessuser.objects.none()
    context={
        'products':Product.objects.all().order_by('-date_posted'),
        'services':Service.objects.all().order_by('-date_posted'),
        'restaurants':Restaurant.objects.all().order_by('-date_posted'),
        'setbs' : Businessuser.objects.all()
    }
    return render(request, 'home/index.html', context)
def contant(request):
    if request.method == 'POST':
        form = ContantForm(request.POST, None)
        if form.is_valid():
            form.save()
            form = ContantForm()
            messages.success(request, f'You have successfuly sent a message we will get back to you as soon as posible')
            redirect('contact')
    else:
       form = ContantForm()
   
    context={
        'form':form
    }
    return render(request, 'home/contact.html', context)

def about(request):
    return render(request, 'home/about-us.html')



def search(request):
    query = request.GET.get('search', None)
    count = 0
    if query:
        pro = ( Q(product_name__icontains=query) | Q(price__icontains=query))
        ser = ( Q(service_name__icontains=query) | Q(price__icontains=query))
        fo = ( Q(food_name__icontains=query) | Q(price__icontains=query))
        context = {
            'products': Product.objects.filter(pro).distinct(),
            'services': Service.objects.filter(ser).distinct(),
            'foods': Restaurant.objects.filter(fo).distinct(),
            'count':len(Product.objects.filter(pro).distinct())+len(Service.objects.filter(ser).distinct())+len(Restaurant.objects.filter(fo).distinct()),
            'query':query
        }
    else:
        context={}
    return render(request, 'home/search.html', context)

def terms(request):
    return render(request, 'bshome/termsandconditions.html')


    

        
