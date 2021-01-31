from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Blog,
    BlogComment,
    AnonyComment,
    Amaizing,


)
from django.views.generic import ( 
            ListView, 
            DetailView,
            CreateView,
            UpdateView,
            DeleteView
            
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import CommentForm, AnonyCommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.contrib import admin





class AmaizingListView(ListView):
    model = Amaizing
    template_name = 'amaizing/blog.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 12


class AmaizingCreateView(LoginRequiredMixin, CreateView):
    model = Amaizing
    template_name ='amaizing/amaizing_form.html'
    fields = ['the_photo', 'title', 'link','content','hashtag']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class AmaizingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Amaizing
    template_name ='amaizing/amaizing_form.html'
    fields = ['the_photo', 'title', 'link','content','hashtag']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AmaizingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Amaizing 
    template_name='amaizing/blog_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):
        return reverse_lazy('amaizing')

def amaizing_single(request, id=None):
    blog = get_object_or_404(Amaizing, id=id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.author = request.user
                obj.code = id
                obj.save()
                form = CommentForm()
                redirect('amaizing-single', id)
                
                
        else:
            form = CommentForm()
        
        
        
    else:
        if request.method == 'POST':
            form = AnonyCommentForm(request.POST, None)
            if form.is_valid():
                obj = form.save( commit = False)
                obj.author = blog.author.username
                obj.code = id
                obj.save()
                form = AnonyCommentForm()
                redirect('amaizing-single', id)
                
                
        else:
            form = AnonyCommentForm()
        
        
    context = {
            'form' : form,
            'comments': BlogComment.objects.filter(code=id).order_by('-date_posted'),
            'comnts': AnonyComment.objects.filter(code=id).order_by('-date_posted'),
            'comment':len(BlogComment.objects.filter(code=id)) + len(AnonyComment.objects.filter(code=id)),
            'code': id,
            'blog':blog,
            

        }
    return render(request, 'amaizing/blog_detail.html', context)


class BlogCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogComment 
    template_name='amaizing/blogcomment_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):
        post = self.get_object()
        id = post.code
        messages.success(self.request, 'You have successfully deleted the comment')
        return reverse_lazy('amaizing-single', kwargs={'id':id})

class BlogAnonyCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AnonyComment 
    template_name='amaizing/blogcomment_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.author:
            return True
        return False
    def get_success_url(self):
        post = self.get_object()
        id = post.code
        messages.success(self.request, 'You have successfully deleted the comment')
        return reverse_lazy('amaizing-single', kwargs={'id':id})



    
