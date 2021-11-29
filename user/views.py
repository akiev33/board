from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register_view(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form.save()
        return redirect('index')

    return render(request, 'users/register.html', locals())
