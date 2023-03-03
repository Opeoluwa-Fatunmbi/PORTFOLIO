from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # add any other URL patterns for your app here
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
