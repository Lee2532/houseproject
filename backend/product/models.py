from django.db import models

class Product(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="상품명")
    brand = models.CharField(max_length=50, null=False, blank=False, verbose_name="브랜드 명")
    content = models.CharField(max_length=200, null=False, blank=False, verbose_name="본문")
    price =  models.IntegerField(blank=False, verbose_name="가격")
    stars =  models.FloatField(blank=False, verbose_name="별점")
    reviews = models.CharField(max_length=100, null=False, blank=False, verbose_name="리뷰")
    
    class Meta:
        db_table = "product"
        managed = False