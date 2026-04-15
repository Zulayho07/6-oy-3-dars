from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

def about(request: HttpRequest):
    data = {
        "company": "My Company",
         "address": "Tashkent",
        "phone": "+998901234567",
        "email": "info@gmail.com"
    }
    return render(request, "main/about.html", data)


