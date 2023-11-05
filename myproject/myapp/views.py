from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')  # Отправить страницу в шаблон для отображения


def flowers(request):
    return render(request, 'myapp/flowers.html')


def about(request):
    return render(request, 'myapp/about.html')


def delivery(request):
    return render(request, 'myapp/delivery.html')


def place_an_order(request):
    return render(request, 'myapp/place_an_order.html')