from django.urls import path
from .views import (about, home, news_by_category, news_detail)

urlpatterns=[
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('categories/<int:category_id>/', news_by_category, name='news_by_category'),
]