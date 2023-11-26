from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginn,name="login"),
    path('success/',views.success, name='success'),
    path('invalid/',views.invalid, name='invalid')
]