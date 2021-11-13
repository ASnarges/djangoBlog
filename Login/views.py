from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def Login_list(request):
    articles = models.Article.objects.all().order_by('date')

    args = {'articles': articles}
    return render(request, 'Login/Loginlist.html',args)

def Login_detail(request, slug):
    return HttpResponse(slug)
