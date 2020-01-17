from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Blog,Maxim
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin
import random



def maximfunc(request):
    if request.method == 'GET':
        maxim = {'saying2':'はよ映らんかい'}
        # saying_pk = Maxim.objects.filter(pk)
        # maxim = {
        #     'saying': Maxim.objects.get(id=saying_pk),
        # }
        return render(request, 'templates/base.html',maxim)

    # def list_view(request):
#     # data2 = ['hello',' world']
#     # data3 = data2[1]
#     # data = Ad.objects.all().values()
#     Facebook_theme = Ad.objects.select_related().values('Facebook__theme','get_date').distinct().order_by('get_date')
#     params = {
#         'data2':Facebook_theme
#         }
#     return render(request, 'app/date_list.html',params)


class maxim:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countmaxim = len(Maxim.objects.all())
        randomint = random.randint(1,countmaxim)
        context.update({
            'saying': Maxim.objects.get(id=randomint),
            'more_context': Maxim.objects.all(),
        })
        return context

        #基本的に多重継承は推奨されていません。複雑化の原因になるので。書き換えたい
        
        #また、上記のような書き方だとデータを一括して取ってきているので、よろしくない。
        #今登録されているPKをとる



class BlogListView(ListView):
    model = Blog
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countmaxim = len(Maxim.objects.all())
        # randomint = random.randrange(1,countmaxim+1)
        randomint = random.randint(1,countmaxim)
        # print(randomint)
        context.update({
            'saying': Maxim.objects.get(id=randomint),
            'more_context': Maxim.objects.all(),
        })
        # blog_list = MyBlog.objects.all().order_by('-publishing_date')[:5]
        return context

    # def get_queryset(self, **kwargs):
    #     saying = super().get_queryset(**kwargs)
    #     print(saying)
    #     return saying



class BlogDetailView(DetailView,maxim):
    model = Blog


def profilefunc(request):
    return render(request,'profile.html')


class BlogCreateView(maxim,LoginRequiredMixin,CreateView):
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


class BlogUpdateView(maxim,LoginRequiredMixin,UpdateView):
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