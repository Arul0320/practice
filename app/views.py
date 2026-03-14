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
    return render(request, 'session.html', {'name': request.session['username']})


# 3 Cookie Example
def cookie_demo(request):
    response = render(request, 'cookie.html')
    response.set_cookie('site', 'DjangoLab')
    return response


# 4 Display Cookie
def cookie_show(request):
    data = request.COOKIES.get('site')
    return render(request, 'cookie_show.html', {'data': data})


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

    send_mail(
        "Test Email from Django",
        "This email is sent using SMTP configuration.",
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False
    )

    return render(request, 'email.html')


# 8 Retrieve Data from Database
def show_contacts(request):

    contacts = Contact.objects.all()

    return render(request, 'contacts.html', {'contacts': contacts})