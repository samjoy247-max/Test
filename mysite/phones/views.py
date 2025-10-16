from django.shortcuts import render, redirect


from .forms import PhoneForm
from .models import Phone

from .models import Phone
def create_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhoneForm()
        return render(request, 'form.html', {'form': form})


def update_phone(request,i_id):
    phone = Phone.objects.get(pk=i_id)
    if request.method == 'POST':
        form = PhoneForm(request.POST,instance=phone )
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhoneForm(instance=phone)
        return render(request, 'form.html', {'form': form})


def delete_phone(request,i_id):
    phone = Phone.objects.get(pk=i_id).delete()
    return redirect('/')
