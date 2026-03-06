from django.contrib import admin
from django.urls import path, include  # 必須要有 include 才能連到 shop

urlpatterns = [
    # 1. 後台管理系統 (這行通常本來就有)
    path('admin/', admin.site.urls),
    
    # 2. 這是最重要的！把首頁跟所有商品相關網址「外包」給 shop 部門處理
    path('', include('shop.urls')), 
]