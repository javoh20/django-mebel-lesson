from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name = 'home'),
    path('about/', About, name = 'about'),
    path('blog/', Blog, name = 'blog'),
    path('contact/', Contact, name = 'contact'),
    path('furniture/', Furniture, name = 'furniture'),
]
