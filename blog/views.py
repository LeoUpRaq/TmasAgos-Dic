from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_admin.html', context)
    
class BlogInit (View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'index.html', context)