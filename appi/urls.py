from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('', views.article_list, name='article_list'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/<int:id>/update/', views.article_update, name='article_update'),
    path('article/<int:id>/delete/', views.article_delete, name='article_delete'),
    path('article/form/', views.article_form, name='article_form'),
    
]
   