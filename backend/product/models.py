from pyexpat import model
from django.db import models

class Product(models.Model):
    idx = models.AutoField(primary_key=True, verbose_name="상품코드")
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="상품명")
    brand = models.CharField(max_length=50, null=False, blank=False, verbose_name="브랜드명")
    content = models.CharField(max_length=200, null=False, blank=False, verbose_name="본문")
    price =  models.IntegerField(blank=False, verbose_name="가격")
    
    class Meta:
        db_table = "product"
        managed = False
        
class ProductReviews(models.Model):
    '''
    추후 구매자 idx, 및 이미지 칼럼 추가 예정
    '''
    product_idx = models.ForeignKey(Product, verbose_name="상품_코드", on_delete=models.CASCADE)
    idx = models.AutoField(primary_key=True, verbose_name="리뷰idx")
    stars =  models.FloatField(blank=False, verbose_name="별점")
    reviews = models.CharField(max_length=100, null=False, blank=False, verbose_name="리뷰")
    
    class Meta:
        db_table = "product_reviews"
        managed = False