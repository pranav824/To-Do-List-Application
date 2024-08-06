from django.urls import path
from .views import index, add, complete, delete, update

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('complete/<int:pk>', complete, name='complete'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>', update, name='update'),

]
