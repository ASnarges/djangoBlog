from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


def User_list(request):
    userha = models.User_signup.objects.all().order_by('name')
    args = {'userha': userha}

    return render(request, 'Login/Loginlist.html', args)


def createsignup(request):
    if request.method == 'POST':
        form = forms.CreateSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login:list')
    else:
        form = forms.CreateSignup()
    return render(request, 'Login/create_signup.html', {'form': form})


def profile(request, id):
    profile = models.User_signup.objects.get(id=id)
    if request.method == 'POST':
        formedit = forms.CreateSignup(request.POST)
        if formedit.is_valid():
            profile.delete()
            formedit.save()
            return redirect('Login:list')
    else:
        formedit = forms.CreateSignup()
    return render(request, 'Login/profile.html', {'profile': profile, 'id': id})


def edit(request, id):
    if request.method == 'POST':
        form = forms.CreateSignup(request.POST)
        form.save()
        return redirect('Login:list')
    else:
        person = models.User_signup.objects.get(id=id)
        form = forms.CreateSignup(instance=person)
        person.delete()
    return render(request, 'Login/edit.html', {'form': form})
