from django.shortcuts import render
from .models import productViews1, productViews2, news

# Create your views here.
def index(requsets):
    view = productViews1.objects.all()
    view2 = productViews2.objects.all()
    new = news.objects.all()

    context ={
        'view': view,
        'view2': view2,
        'new': new
    }
    return render(requsets, 'index.html', context)