from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)       # 蟲的名字
    price = models.IntegerField()                  # 價格 (整數)
    description = models.TextField()               # 商品詳細描述
    stock = models.IntegerField(default=0)        # 庫存數量
    image_url = models.URLField(blank=True)        # 蟲的照片網址
    class Category(models.Model):
        name = models.CharField(max_length=200)
        

    def __str__(self):
        return self.name