from django.urls import path,include
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',BlogListView.as_view(), name="index"),
    path('<int:pk>',BlogDetailView.as_view(), name="detail"),
    path('create',BlogCreateView.as_view(),name='create'),
    path('<int:pk>/update',BlogUpdateView.as_view(),name="update"),
    path('<int:pk>/delete',BlogDeleteView.as_view(),name='delete'),
    
    path('login/',LoginView.as_view(template_name="login.html"), name="login"),
    path('logout',LogoutView.as_view(template_name="logout.html"), name="logout"),

]