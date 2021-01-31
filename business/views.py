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

from .models import User,Businessuser
from django.db.utils import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from .decorators import business_required
from django.utils.decorators import method_decorator
from home.models import OrderProduct, OrderFood, BookService

from business.form import (
    BusinessSignUpForm,
    UserSignUpForm,
    UserUpdateForm,
    UpdateProfile,
    CreateBusinessuser
    
)
from .decorators import business_required,justuser_required
from home.models import BusinessActivator



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class BusinessSignUpView(CreateView):
    model = User
    form_class = BusinessSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'My Business'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        p=BusinessActivator.objects.create(bussiness=user,service=True, product=True, food=True)
        p.save()
        return redirect('set-business', user.username)



@login_required
@business_required
def setbusiness(request, username=None):
    user = get_object_or_404(User, username=username)
    try:
        if request.method == 'POST':
            form = CreateBusinessuser(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.author = request.user
                obj.code = username
                obj.save()
                form = CreateBusinessuser()
                messages.success(request, f'Your account have been successfully created and what your business does')
                return redirect('home')
                        
        else:
            form = CreateBusinessuser()
        context = {
            'form':form
        }
        return render(request, 'home/businessuser_form.html', context)
    except IntegrityError:
        
        return redirect('update-set-business',username)
@login_required
@business_required
def updatesetbusiness(request, code=None):
    obj = get_object_or_404(Businessuser, code=code)
    form = CreateBusinessuser(request.POST or None, instance = obj)
    if form.is_valid():     
        form.save()
        messages.success(request, f'You have successfully updated')
        return redirect('home')
    context={
        'form':form
    }
    return render(request, 'home/businessuser_form.html', context)



class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'My Personal Account'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')
        

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account have been successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'bshome/profile.html', context)
def terms(request):
    return render(request, 'bshome/termsandconditions.html')


