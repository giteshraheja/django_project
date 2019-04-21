from django.shortcuts import render
from About.models import Banner
from .models import Blogger
# Create your views here.

def Blog(request):
    context = {
        'Banners': Banner.objects.all(),
        'Blogs': Blogger.objects.all(),
    }

    return render(request, 'Blog/blog.html', context)