from django.shortcuts import render

# Create your views here.

def apply(request):
    return render(request, 'main/apply.html')