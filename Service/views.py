from django.shortcuts import render

# Create your views here.
from About.models import Banner


def service(request):
    context = {
        'Banners': Banner.objects.all()
    }

    return render(request, 'Service/services.html', context)


def terms(request):
    return render(request, 'Service/terms.html')


def privacy(request):
    return render(request, 'Service/terms.html')
