from django.contrib import admin

from .models import Banner, aboutus, questions

# Register your models here.

admin.site.register(Banner)
admin.site.register(aboutus)
admin.site.register(questions)