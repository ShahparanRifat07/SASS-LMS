from django.urls import path
from .views import index,sign_up,sign_in

app_name = 'user'

urlpatterns = [
    path('',index,name='index'),
    path('signup/',sign_up,name='create-user'),
    path('signin/',sign_in,name='login')
]