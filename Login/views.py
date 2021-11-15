from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
# def Login_list(request):
#     #articles = models.Article.objects.all().order_by('-date')
#     userr = models.User.objects.all()
#     args = {'userr': userr}
#
#     #args = {'articles': articles}
#     return render(request, 'Login/Loginlist.html',args)

def User_list(request):
    userha= models.User_signup.objects.all().order_by('name')
    args = {'userha': userha}

    return render(request, 'Login/Loginlist.html',args)


def Login_detail(request, slug):
    # return HttpResponse(slug)
    login= models.Article.objects.get(slug=slug)
    return render(request, 'Login/Login_detail.html', {'Login':login})

def createsignup (request):
    if request.method == 'POST':
        form = forms.CreateSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login:list')
    else:
        form = forms.CreateSignup()
    return render(request, 'Login/create_signup.html', {'form':form} )

def profile(request, name):
    profile = models.User_signup.objects.get(name=name)
    # if request.method == 'POST':
    #     return render(request, 'Login/edit.html', {'edit: '})
    # else:
    if request.method== 'POST':
        formedit= forms.CreateSignup(request.POST)
        if formedit.is_valid():
            profile.delete()
            formedit.save()
            # instanc = formedit.save(commit=False)
    #         # INja shart bezaram
    #         formedit.save()
            return redirect('Login:list')
    else:
        formedit = forms.CreateSignup()
    return render(request, 'Login/profile.html', {'profile': profile , 'form': formedit})

@login_required(login_url="/accounts/login2")
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save()
            return redirect('Login:list')
    else:
        form = forms.CreateArticle()

    return render(request, 'Login/create_article.html', {'form': form})