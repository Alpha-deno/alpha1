from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .form import (
    OrderProductForm, 
    OrderFoodForm, 
    BookServiceForm,
    NonUserOrderProductForm,
    NonUserOrderFoodForm,
    NonUserBookServiceForm

)
from .models import (
    Product, 
    Service, 
    Restaurant, 
    OrderProduct, 
    OrderFood, 
    BookService,
    NonUserBookService,
    NonUserOrderFood,
    NonUserOrderProduct
    )
from datetime import datetime
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from business.models import User, Businessuser
from django.urls import reverse_lazy,reverse
from django.core.mail import send_mail

def orderproduct(request, username=None):
    user = get_object_or_404(User, username=username)
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            
            

            form = OrderProductForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.author = request.user
                obj.code = username
                obj.save()
                form = OrderProductForm()
                
                prod='Get full detail on your business home page'
                messages.success(request, f'You have successfuly placed an order')
                #send_mail( f'New order from {request.user}' , prod, 'ituromunyu@gmail.com', ['ituromunyu@gmail.com'], fail_silently = False )
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
    else:
        if request.method == 'POST':
            form = NonUserOrderProductForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.code = username
                obj.save()
                form = NonUserOrderProductForm()
                prod='Get full detail on your business home page'
                messages.success(request, f'You have successfuly placed an order')
                #send_mail( f'New order from {request.user}' , prod, 'ituromunyu@gmail.com', ['ituromunyu@gmail.com'], fail_silently = False )

                return redirect('sb-product',username) 

        else:
            form = NonUserOrderProductForm()

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
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderFoodForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.author = request.user
                obj.code = username
                obj.save()
                form = OrderFoodForm()
                prod='Get full detail on your business home page'
                messages.success(request, f'You have successfuly placed an order')
                #send_mail( f'New order from {request.user}' , prod, 'ituromunyu@gmail.com', ['ituromunyu@gmail.com'], fail_silently = False )

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
    else:
        if request.method == 'POST':
            form = NonUserOrderFoodForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.code = username
                obj.save()
                form = NonUserOrderFoodForm()
                prod='Get full detail on your business home page'
                messages.success(request, f'You have successfuly placed an order')
                #send_mail( f'New order from {request.user}' , prod, 'ituromunyu@gmail.com', ['ituromunyu@gmail.com'], fail_silently = False )

                return redirect('sb-food',username)

        else:
            form = NonUserOrderFoodForm()

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
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookServiceForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.author = request.user
                obj.code = username
                obj.save()
                form = BookServiceForm()
                prod='Get full detail on your business home page'
                #send_mail( f'New order from {request.user}' , prod, 'ituromunyu@gmail.com', ['ituromunyu@gmail.com'], fail_silently = False )

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
    else:
        if request.method == 'POST':
            form = NonUserBookServiceForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.code = username
                obj.save()
                form = NonUserBookServiceForm()
                messages.success(request, f'You have successfuly booked')
                prod='Get full detail on your business home page'
                #send_mail( f'New order from {request.user}' , prod, 'ituromunyu@gmail.com', ['ituromunyu@gmail.com'], fail_silently = False )

                return redirect('sb-service',username)

        else:
            form = NonUserBookServiceForm()

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

#non user delete classes

class OrderproductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = NonUserOrderProduct
   template_name='bshome/prorder_con_delete.html'
   def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.code:
            return True
        return False
   def get_success_url(self):
        messages.success(self.request, 'You have successfully deleted the Order')
        username = self.request.user.username
        return reverse('sb-product', kwargs={'username':username})
        
class OrderfoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = NonUserOrderFood
   template_name='bshome/foodorder_con_delete.html'
   
   def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.code:
            return True
        return False
   def get_success_url(self):
        username = self.request.user.username
        messages.success(self.request, 'You have successfully deleted the Order')
        return reverse_lazy('sb-food', kwargs={'username':username})

class BookserviceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = NonUserBookService
   template_name='bshome/serorder_con_delete.html'
   
   def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.code:
            return True
        return False
   def get_success_url(self):
        messages.success(self.request, 'You have successfully deleted the booked service')       
        username = self.request.user.username
        return reverse('sb-service', kwargs={'username':username})
