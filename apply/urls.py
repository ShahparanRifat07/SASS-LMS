from django.urls import path
from .views import apply

app_name = 'apply'

urlpatterns = [
    path('apply-institution/',apply,name="apply-institution"),
]