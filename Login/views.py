from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def Login_list(request):
    articles = models.Article.objects.all().order_by('-date')

    args = {'articles': articles}
    return render(request, 'Login/Loginlist.html',args)


def Login_detail(request, slug):
    # return HttpResponse(slug)
    login= models.Article.objects.get(slug=slug)
    return render(request, 'Login/Login_detail.html', {'Login':login})

@login_required(login_url="/accounts/login2")
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('Login:list')
    else:
        form = forms.CreateArticle()

    return render(request, 'Login/create_article.html', {'form': form})