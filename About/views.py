from django.shortcuts import render

from . import models as about_models
# Create your views here.

def About(request):
    context = {
        'Banners' : about_models.Banner.objects.all(),
        'Aboutus' : about_models.aboutus.objects.all(),
        'question' : about_models.questions.objects.all(),
    }
    return render(request, 'About/about.html', context)