from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ed', views.ed, name='ed'),
    path('<str:name>', views.greet, name='greet')
]
