from django.urls import path
from .views import homePageView,contactPageView

urlpatterns = [
    path('home', homePageView, name='home'),
    path('contact', contactPageView, name='contact'),    
]
