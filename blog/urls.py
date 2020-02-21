from django.urls import path #импортировали функцию path
from .  import views #импортировали все представления

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
