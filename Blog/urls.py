from django.conf.urls import url

from . import views as Blog_views

urlpatterns = [

    url(r'^$', Blog_views.Blog),

]