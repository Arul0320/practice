from datetime import datetime

from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

# 1 Home Page
def home(request):
    return render(request, 'home.html')


# 2 Session Example
def session_demo(request):
    request.session['username'] = "Student"
    request.session['login_time'] = str(datetime.now())

    context = {
        'name': request.session['username'],
        'time': request.session['login_time']
    }
    return render(request, 'session.html', context)


# 3 Cookie Example
def cookie_demo(request):
    response = render(request, 'cookie.html')
    response.set_cookie('site', 'DjangoLab')
    response.set_cookie('visit_time', str(datetime.now()))
    return response


# 4 Display Cookie
def cookie_show(request):
    data = request.COOKIES.get('site')
    visit_time = request.COOKIES.get('visit_time')
    context = {
        'site': data,
        'visit_time': visit_time
    }
    return render(request, 'cookie_show.html', context)


# 5 Contact Form (Save to DB)
def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# 6 Contact Success Page
def contact_success(request):
    return render(request, 'success.html')


# 7 Send Email using SMTP
def send_email_view(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get('name')
    
        send_mail(
            "Test Email",
            f"Hello {name}, this is a test email from Django.",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        
        message = "Email sent successfully!" 

    return render(request, 'email.html' , {'message': message})


# 8 Retrieve Data from Database
def show_contacts(request):

    contacts = Contact.objects.all()

    return render(request, 'contacts.html', {'contacts': contacts})