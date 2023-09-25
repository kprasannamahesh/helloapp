from django.urls import path
from .views import homePageView,contactPageView, aboutMe, checkPostsViews

urlpatterns = [
    path('', homePageView, name='home'),
    path('contact/', contactPageView, name='contact'),
    path('about/',aboutMe, name='about'),
    path('posts/',checkPostsViews, name='about'),
]
