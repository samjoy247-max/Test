from django.shortcuts import render
from phones.models import Phone


def home(request):
    phones = Phone.objects.all()
    return render(request, 'home.html',context={'phones':phones})

