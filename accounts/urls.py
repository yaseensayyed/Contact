from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUp, name='signup'),
    path('login/', LogIn, name='login'),
    path('dashboard/', dash, name='dashboard'),
    path('logout',LogOut,name='logout')
    
]

