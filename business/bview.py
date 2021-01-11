from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ( 
            ListView, 
            DetailView,
            CreateView,
            UpdateView,
            DeleteView,
            TemplateView
            
)
from django.utils.decorators import method_decorator
from .models import User,BusinessComment,Businessuser
from home.models import (
    Product,
    Service,
    Restaurant,
    OrderProduct,
    OrderFood,
    BookService,
    BusinessActivator
)
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .decorators import business_required
from .form import CreateBusinessComment
 
  

@method_decorator([login_required, business_required], name='dispatch')
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_image', 'product_name', 'price','about_product', 'new', 'offer', 'offer_price']
    def get_context_data(self, *args, **kwargs):
        context = super(ProductCreateView, self).get_context_data( *args, **kwargs)
        usr = self.request.user
        context['activated'] = BusinessActivator.objects.filter(bussiness=usr)
        context['setbs'] = Businessuser.objects.filter(author=usr)
        return context
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
	    
        if 'add_product' in self.request.POST:
            messages.success(self.request, 'You have successfully added product')
            return reverse_lazy('product-create')
        elif 'save_product' in self.request.POST:
            messages.success(self.request, 'You have successfully added product')
            username = self.request.user.username
            return reverse('sb-product', kwargs={'username':username})
    
        


    
    


@method_decorator([login_required, business_required], name='dispatch')
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['product_image', 'product_name', 'price', 'about_product','new', 'offer', 'offer_price']
    def get_context_data(self, *args, **kwargs):
        context = super(ProductUpdateView, self).get_context_data( *args, **kwargs)
        usr = self.request.user
        context['activated'] = BusinessActivator.objects.filter(bussiness=usr)
        context['setbs'] = Businessuser.objects.filter(author=usr)
        return context
    def form_valid(self, form):
        messages.success(self.request, 'You have successfully updated product')
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):
	    
        if 'add_product' in self.request.POST: 
            messages.success(self.request, 'You have successfully added product')  
            return reverse_lazy('product-create')
        elif 'save_product' in self.request.POST:
            username = self.request.user.username
            return reverse('sb-product', kwargs={'username':username})



@method_decorator([login_required, business_required], name='dispatch')
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name='bshome/product_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@method_decorator([login_required, business_required], name='dispatch')
class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    fields = ['service_image', 'service_name', 'price', 'about_service', 'offer', 'offer_price']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, *args, **kwargs):
        context = super(ServiceCreateView, self).get_context_data( *args, **kwargs)
        usr = self.request.user
        context['activated'] = BusinessActivator.objects.filter(bussiness=usr)
        context['setbs'] = Businessuser.objects.filter(author=usr)
        return context
    def get_success_url(self):	    
        if 'add_service' in self.request.POST:
            messages.success(self.request, 'You have successfully added service')
            return reverse_lazy('service-create')
        elif 'save_service' in self.request.POST:
            messages.success(self.request, 'You have successfully added service')
            username = self.request.user.username
            return reverse('sb-service', kwargs={'username':username})
        



@method_decorator([login_required, business_required], name='dispatch')
class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['service_image', 'service_name', 'price', 'about_service', 'offer', 'offer_price']
    def get_context_data(self, *args, **kwargs):
        context = super(ServiceUpdateView, self).get_context_data( *args, **kwargs)
        usr = self.request.user
        context['activated'] = BusinessActivator.objects.filter(bussiness=usr)
        context['setbs'] = Businessuser.objects.filter(author=usr)
        return context
    def form_valid(self, form):
        messages.success(self.request, 'You have successfully Updated service')
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):	    
        if 'add_service' in self.request.POST:
            messages.success(self.request, 'You have successfully added service')
            return reverse_lazy('service-create')
        elif 'save_service' in self.request.POST:
            username = self.request.user.username
            return reverse('sb-service', kwargs={'username':username})
 


@method_decorator([login_required, business_required], name='dispatch')
class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    template_name='bshome/service_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@method_decorator([login_required, business_required], name='dispatch')
class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['food_image', 'food_name', 'price', 'about_food', 'breakfast', 'lunch', 'dinner', 'offer', 'offerprice']
    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data( *args, **kwargs)
        usr = self.request.user
        context['activated'] = BusinessActivator.objects.filter(bussiness=usr)
        context['setbs'] = Businessuser.objects.filter(author=usr)
        return context
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):	    
        if 'add_food' in self.request.POST:
            messages.success(self.request, 'You have successfully added item')
            return reverse_lazy('restaurant-create')
        elif 'save_food' in self.request.POST:
            messages.success(self.request, 'You have successfully added item')
            username = self.request.user.username
            return reverse('sb-food', kwargs={'username':username})
 

        



@method_decorator([login_required, business_required], name='dispatch')
class RestaurantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Restaurant
    fields = ['food_image', 'food_name', 'price', 'about_food', 'breakfast', 'lunch', 'dinner', 'offer', 'offerprice']
    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data( *args, **kwargs)
        usr = self.request.user
        context['activated'] = BusinessActivator.objects.filter(bussiness=usr)
        context['setbs'] = Businessuser.objects.filter(author=usr)
        return context
    def form_valid(self, form):
        messages.success(self.request, 'You have successfully updated item')
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):	    
        if 'add_food' in self.request.POST:
            messages.success(self.request, 'You have successfully added item')
            return reverse_lazy('restaurant-create')
        elif 'save_food' in self.request.POST:
            username = self.request.user.username
            return reverse('sb-food', kwargs={'username':username})
    



@method_decorator([login_required, business_required], name='dispatch')
class RestaurantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Restaurant
    template_name='bshome/food_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# product, service, resturant detail view

def product_listview(request, username=None):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CreateBusinessComment(request.POST, None)
        if form.is_valid():
            obj = form.save( commit = False)
            obj.author = request.user
            obj.code = username
            obj.save()
            form = CreateBusinessComment()
            return redirect('sb-product',username)
            
            
    else:
        form = CreateBusinessComment()
    context={
        'products':Product.objects.filter(author=user),
        'form' : form,
        'comments' : BusinessComment.objects.filter(code=username).order_by('-date_posted'),
        'usrname': username,
        'comment' : len(BusinessComment.objects.filter(code=username)),
        'orders' : OrderProduct.objects.filter(code=username).order_by('-date_posted'),
        'order': len(OrderProduct.objects.filter(code=username)),
        'bsuser':Businessuser.objects.filter(code=username),
        'usr':user,
        'activator':BusinessActivator.objects.filter(bussiness=user)

    }
    return render(request, 'bshome/producthome.html', context)

def service_listview(request, username=None):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CreateBusinessComment(request.POST, None)
        if form.is_valid():
            obj = form.save( commit = False)
            obj.author = request.user
            obj.code = username
            obj.save()
            form = CreateBusinessComment()
            return redirect('sb_service', username)
            
            
    else:
        form = CreateBusinessComment()
    context={
        'services':Service.objects.filter(author=user),
        'form' : form,
        'comments' : BusinessComment.objects.filter(code=username).order_by('-date_posted'),
        'usrname': username,
        'comment' : len(BusinessComment.objects.filter(code=username)),
        'orders' : BookService.objects.filter(code=username).order_by('-date_posted'),
        'order' : len(BookService.objects.filter(code=username)),
        'bsuser':Businessuser.objects.filter(code=username),
        'usr':user,
        'activator':BusinessActivator.objects.filter(bussiness=user)
    }
    return render(request, 'bshome/servicehome.html', context)

def restaurant_listview(request, username=None):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CreateBusinessComment(request.POST, None)
        if form.is_valid():
            obj = form.save( commit = False)
            obj.author = request.user
            obj.code = username
            obj.save()
            form = CreateBusinessComment()
            return redirect('sb_hotel', username)
            
            
    else:
        form = CreateBusinessComment()
    context={
        'foods':Restaurant.objects.filter(author=user),
        'form' : form,
        'comments' : BusinessComment.objects.filter(code=username).order_by('-date_posted'),
        'usrname': username,
        'comment' : len(BusinessComment.objects.filter(code=username)),
        'orders': OrderFood.objects.filter(code=username).order_by('-date_posted'),
        'order': len(OrderFood.objects.filter(code=username)),
        'bsuser':Businessuser.objects.filter(code=username),
        'usr':user,
        'activator':BusinessActivator.objects.filter(bussiness=user)
    }
    return render(request, 'bshome/hotelhome.html', context)
class BusinessCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BusinessComment 
    template_name='bshome/businesscomment_confirm_delete.html'
    success_url = 'home'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):
      
        messages.success(self.request, 'You have successfully deleted the comment')
        return reverse_lazy('home')
