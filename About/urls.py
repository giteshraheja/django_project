from django.conf.urls import url

from . import views as About_views

urlpatterns = [

    url(r'^$', About_views.About),
]