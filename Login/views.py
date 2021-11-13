from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required


# Create your views here.
def Login_list(request):
    articles = models.Article.objects.all().order_by('-date')

    args = {'articles': articles}
    return render(request, 'Login/Loginlist.html',args)


def Login_detail(request, slug):
    # return HttpResponse(slug)
    login= models.Article.objects.get(slug=slug)
    return render(request, 'Login/Login_detail.html',{'Login':login})

@login_required(login_url="/accounts/login2")
def create_article(request):
    return render(request, 'Login/create_article.html')