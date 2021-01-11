from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .form import OrderProductForm, OrderFoodForm, BookServiceForm
from .models import Product, Service, Restaurant, OrderProduct, OrderFood, BookService
from datetime import datetime
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from business.models import User, Businessuser
from django.urls import reverse_lazy,reverse

def orderproduct(request, username=None):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = OrderProductForm(request.POST, None)
        if form.is_valid():
            obj = form.save( commit = False)
            obj.author = request.user
            obj.code = username
            obj.save()
            form = OrderProductForm()
            messages.success(request, f'You have successfuly placed an order')
            return redirect('sb-product',username) 

    else:
        form = OrderProductForm()

    context={
        'form':form,
        'products': Product.objects.filter(author=user),
        'usrname': username,
        'bsuser':Businessuser.objects.filter(code=username),
        'usr':user

    }
    return render(request, 'home/orderproduct.html', context)

def orderfood(request, username=None):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = OrderFoodForm(request.POST, None)
        if form.is_valid():
            obj = form.save( commit = False)
            obj.author = request.user
            obj.code = username
            obj.save()
            form = OrderFoodForm()
            messages.success(request, f'You have successfuly placed an order')
            return redirect('sb-food',username)

    else:
        form = OrderFoodForm()

    context={
        'form':form,
        'foods': Restaurant.objects.filter(author=user),
        'usrname': username,
        'bsuser':Businessuser.objects.filter(code=username),
        'usr':user

    }
    return render(request, 'home/orderfood.html', context)

def bookservice(request, username=None):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = BookServiceForm(request.POST, None)
        if form.is_valid():
            obj = form.save( commit = False)
            obj.author = request.user
            obj.code = username
            obj.save()
            form = BookServiceForm()
            messages.success(request, f'You have successfuly booked')
            return redirect('sb-service',username)

    else:
        form = BookServiceForm()

    context={
        'form':form,
        'services': Service.objects.filter(author=user),
        'usrname': username,
        'bsuser':Businessuser.objects.filter(code=username),
        'usr':user

    }
    return render(request, 'home/bookservice.html', context)

class OrderProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = OrderProduct
   template_name='bshome/prorder_confirm_delete.html'
   def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.code:
            return True
        return False
   def get_success_url(self):
        messages.success(self.request, 'You have successfully deleted the Order')
        username = self.request.user.username
        return reverse('sb-product', kwargs={'username':username})
        
class OrderFoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = OrderFood
   template_name='bshome/foodorder_confirm_delete.html'
   
   def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.code:
            return True
        return False
   def get_success_url(self):
        username = self.request.user.username
        messages.success(self.request, 'You have successfully deleted the Order')
        return reverse_lazy('sb-food', kwargs={'username':username})

class BookServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = BookService
   template_name='bshome/serorder_confirm_delete.html'
   success_url = 'home'
   def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.code:
            return True
        return False
   def get_success_url(self):
        messages.success(self.request, 'You have successfully deleted the booked service')       
        username = self.request.user.username
        return reverse('sb-service', kwargs={'username':username})
