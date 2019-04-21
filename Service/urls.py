from django.conf.urls import url

from . import views as Service_views

urlpatterns = [

    url(r'^$', Service_views.service),
    url(r'^terms/$', Service_views.terms),
    url(r'^privacy/$', Service_views.privacy),
]