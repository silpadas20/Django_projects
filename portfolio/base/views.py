from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Cert
# Create your views here.

def home(request):
	return render(request, 'base/index.html')

def certs(request):
	certs = Cert.objects.all()
	context = {'certs':certs}
	return render(request, 'base/certs.html', context)

def profile(request):
	return render(request, 'base/profile.html')

def aboutme(request):
	return render(request, 'base/about.html')

def skills(request):
	return render(request, 'base/skills.html')

def contact(request):
	return render(request, 'base/contact.html')

def sendEmail(request):
	if request.method == 'POST':
		template = render_to_string('base/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['mailtosilpadas@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'base/email_sent.html')
