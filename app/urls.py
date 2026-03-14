from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),

    path('session/', views.session_demo, name="session"),

    path('cookie/', views.cookie_demo, name="cookie"),
    path('showcookie/', views.cookie_show, name="showcookie"),

    path('contact/', views.contact_form, name="contact"),
    path('success/', views.contact_success, name="contact_success"),

    path('sendemail/', views.send_email_view, name="send_email"),

    path('contacts/', views.show_contacts, name="contacts"),

]