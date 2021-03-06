from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blogs/',views.BlogListView.as_view(),name='blogs'),
    path('blogs/<int:pk>',views.BlogDetailView.as_view(),name='blog-detail'),
    path('authors/',views.BlogAuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>',views.BlogAuthorDetailView.as_view(),name='blogs-by-author'),

]