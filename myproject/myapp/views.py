from django.shortcuts import render, get_object_or_404
from .models import Product



def home(request):
    products = Product.objects.all()  # Получаем все объекты модели Product из базы данных
    return render(request, 'myapp/home.html', context={'products': products})

def flowers(request):
    return render(request, 'myapp/flowers.html')


def about(request):
    return render(request, 'myapp/about.html')


def delivery(request):
    return render(request, 'myapp/delivery.html')


def place_an_order(request):
    return render(request, 'myapp/place_an_order.html')


def roses(request):
    return render(request, 'myapp/roses.html')

def roses(request, producttt_id):
    producttt = get_object_or_404(Product, id=producttt_id)
    return render(request, 'myapp/roses.html', {'producttt': producttt})
