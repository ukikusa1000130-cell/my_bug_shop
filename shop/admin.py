from django.contrib import admin
from .models import Product  # 把剛才設計的蟲子模型引進來

# 讓 Product (商品) 出現在管理後台
admin.site.register(Product)
