from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('about/', About),
    path('blog/', Blog),
    path('contact/', Contact),
    path('furniture/', Furniture),
]
