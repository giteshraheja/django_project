from django.shortcuts import HttpResponse
from django.shortcuts import render
from Blog.models import Blogger
from About.models import Banner, aboutus, questions


def index(request):
    context = {
        'Banners': Banner.objects.all(),
        'Blogs': Blogger.objects.all().order_by('-title')[:4],
        'Aboutus': aboutus.objects.all(),
        'Questions': questions.objects.all(),
    }

    return render(request, 'Main/index.html', context)


def running(request):
    # return HttpResponse(
    #     "<h1>Main features of Project Made By: Devesh, Mukul, Gitesh</h1><hr><h1>Changelog:</h1><h2>Version Control Used: Pycharm VCS</h2><h3>Python: v_3.6.8</h3><h3>Django: v_1.11.20</h3><h3>Bootstrap: v_3.3.7</h3><hr><h2>Features Added: </h2><h3>Added ChatBot Validations for Online Interaction</h3><h3>Added Contact us Validations with reCaptcha form offline Interaction</h3><h3>Added 2 step Customer Registration Verification using hidden URL</h3><h3>Made Website online with SSL Https Certificate</h3>")
    return render(request, 'Main/changelog.html')
