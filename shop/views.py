from django.shortcuts import render
from .models import Product
# 1. 商品列表的大腦
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
# 2. 商品詳情的大腦
def product_detail(request, pk):
    product = Product.objects.get(id=pk) # 根據身份證字號(id)找那一隻蟲
    return render(request, 'shop/product_detail.html', {'product': product})
    # 3. 這是你那酷炫彩虹首頁的大腦
def index(request):
    # 指向我們剛剛建立的新檔案
    return render(request, 'shop/index.html')
