import json
import urllib
import requests

from django.contrib import messages
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from About.models import Banner
from . import forms as contact_forms

# Create your views here.

def contact(request):
    if request.method == 'GET':
        form = contact_forms.Contact_form()
    else:
        form = contact_forms.Contact_form(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Name']
            from_mail = form.cleaned_data['Email_Id']
            message = from_mail + "\n" + form.cleaned_data['yourmessage'] + "\n" + subject


            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()


            if result['success']:
                try:
                    send_mail(subject, message, from_mail, ['mkljuneja18@gmail.com'])
                    messages.success(request, 'E-mail Sent successfully!')
                    form = contact_forms.Contact_form()
                except BadHeaderError:
                    messages.error(request, 'Invalid header found.')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    context = {
        'Banners': Banner.objects.all(),

        'form': form
    }

    return render(request, 'Contact/contact.html', context)


