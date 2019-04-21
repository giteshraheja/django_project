from django.conf.urls import url

from . import views as Contact_views

urlpatterns = [

    url(r'^$', Contact_views.contact),
]