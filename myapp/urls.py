from django.urls import path
from .import views

app_name = 'myapp'

urlpatterns = [
    path('index/', views.index , name='index'),
    path('create/', views.create , name='create'),
    path('update/<pk>', views.update , name='update'),
    path('delete/<pk>', views.delete, name='delete'),
]