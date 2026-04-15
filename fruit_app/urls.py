from django.urls import path
from .views import send_fruit_list
urlpatterns= [
    path('', send_fruit_list)
]