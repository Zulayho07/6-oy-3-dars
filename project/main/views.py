from django.shortcuts import render

from django.http import HttpRequest
from .models import Category, News


def home(request: HttpRequest):
    categories=Category.objects.all()
    news=News.objects.all()

    context={
        'categories':categories,
        'news':news,
        'title': 'Yangiliklar'
    }
    return render(request, 'main/index.html', context)


def news_detail(request: HttpRequest, news_id):
    news=News.objects.get(id=news_id)
    context={
        'news': news,
    }

    return render(request, 'main/detail.html', context)


def news_by_category(request: HttpRequest, category_id):
    categories=Category.objects.all()
    category=Category.objects.get(id=category_id)
    news=News.objects.filter(category=category_id)

    context = {
        'news': news,
        'categories':categories,
        'title': category
    }

    return render(request, 'main/index.html', context)


def about(request: HttpRequest):
    data = {
        "company": "My Company",
        "address": "Tashkent",
        "phone": "+998901234567",
        "email": "info@gmail.com"
    }
    return render(request, "main/about.html", data)


