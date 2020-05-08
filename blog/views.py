from django.shortcuts import render
from .models import Blog,BlogAuthor,BlogComment
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    #view function for home page
    num_blogs=Blog.objects.all().count()
    num_authors=BlogAuthor.objects.all().count()
    context={
        'num_blogs':num_blogs,
        'num_authors':num_authors

    }
    return render(request,'index.html',context=context)

from django.views import generic
class BlogListView(generic.ListView):
    model=Blog

class BlogDetailView(LoginRequiredMixin,generic.DetailView):
    model=Blog

class BlogAuthorListView(generic.ListView):
    model=BlogAuthor

class BlogAuthorDetailView(generic.DetailView):
    model=BlogAuthor    
