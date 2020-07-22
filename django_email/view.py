from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    if request.method == 'GET':
        pass
    else:
        email = request.POST['email']
        subject = request.POST['subject']
        content = request.POST['content']

        sender_name = 'Django 2.2'
        email_from = settings.EMAIL_HOST_USER
        sender = sender_name+email_from
        recipient_list = [email, ]
        send_mail(subject, content,sender, recipient_list)
    return render(request,'index.html')

