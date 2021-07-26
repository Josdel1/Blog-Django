from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),    
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<slug>/', views.PostDetailView.as_view(), name='detail'),
]

