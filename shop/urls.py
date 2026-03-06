# shop/urls.py
from django.urls import path
from . import views

# shop/urls.py
urlpatterns = [
    # 1. 網址是空的時候，執行 index 函式，秀出彩虹首頁
    path('', views.index, name='index'), 
    
    # 2. 網址是 products/ 時，執行 product_list，這才是之後放商品的地方
    path('products/', views.product_list, name='product_list'),

    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]