from django.shortcuts import render

# Create your views here.


def home(request):
    context = "Assalom"
    return render(request, 'home.html')
