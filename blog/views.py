from django.shortcuts import render,get_object_or_404,redirect
from .models import (
    Blog,
    BlogComment,
    

)
from django.views.generic import ( 
            ListView, 
            DetailView,
            CreateView,
            UpdateView,
            DeleteView
            
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib import messages




class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 12

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    #template_name ='home/blog_create.html'
    fields = ['the_photo', 'title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['the_photo', 'title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog 
    template_name='blog/blog_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):
        return reverse_lazy('blog')

def blog_single(request, id=None):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST, None)
        if form.is_valid():
            obj = form.save( commit = False)
            obj.author = request.user
            obj.code = id
            obj.save()
            form = CommentForm()
            redirect('blog-single', id)
            
            
    else:
        form = CommentForm()
    
    
    context = {
        'form' : form,
        'comments': BlogComment.objects.filter(code=id).order_by('-date_posted'),
        'comment':len(BlogComment.objects.filter(code=id)),
        'code': id,
        'blog':blog,
        

    }
    return render(request, 'blog/blog_detail.html', context)


class BlogCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogComment 
    template_name='blog/blogcomment_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    def get_success_url(self):
        post = self.get_object()
        id = post.code
        messages.success(self.request, 'You have successfully deleted the comment')
        return reverse_lazy('blog-single', kwargs={'id':id})


    
