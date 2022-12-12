from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store:home')
    else:
        form = UserForm()

    context = {
        'form': form
    }

    return render(request, "users/register.html", context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("store:home")