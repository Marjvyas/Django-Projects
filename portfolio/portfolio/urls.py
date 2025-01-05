from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home),
    path('about-me',views.about),
    path('contact-me',views.contact),
]
