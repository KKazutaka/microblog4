from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(ListView):
    model = Blog
    paginate_by = 3

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    form_class = BlogForm
    # fields = ['content']
    template_name = 'blog/blog_create_form.html'
    success_url = reverse_lazy('index')

    login_url = '/login'

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '保存に失敗しました')
        return super().form_invalid(form)


class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'
    # fields = ['content']

    login_url = '/login'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk":blog_pk})
        return url
    
    def form_valid(self, form):
        messages.success(self.request, '更新されました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '更新に失敗しました')
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('index')

    login_url = '/login'


    def delete(self,request, *args, **kwargs):
        messages.success(self.request, '削除しました')
        return super().delete(request, *args, **kwargs)