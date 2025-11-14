from django.shortcuts import render
from .models import Main
def base(request):
    return render(request, 'base.html')

def home(request):
    malumotlar = Main.objects.all()
    context = {
        'malumotlar': malumotlar,
    }
    return render(request, 'home.html', context)


def Navigation(request):
    return render(request, 'navigation.html')

def footer(request):
    return render(request, 'footer.html')

def orta(request):
    return render(request, 'orta.html')