from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/', views.flowers, name='flowers'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('place_an_order/', views.place_an_order, name='place_an_order'),
    path('roses/', views.roses, name='roses'),
    path('roses/<int:producttt_id>/', views.roses, name='roses'),


]

