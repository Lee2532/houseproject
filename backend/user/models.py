from datetime import datetime
from django.db import models

class User(models.Model):
    idx = models.AutoField(primary_key=True, verbose_name="idx")
    username = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name="유저명")
    password = models.CharField(max_length=200, null=False, blank=False, verbose_name="비밀번호")
    grade = models.CharField(max_length=200, null=False, blank=False, default="user",verbose_name="등급")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="회원가입시간")
    update_date = models.DateTimeField(auto_now=True, verbose_name="수정시간")
    
    class Meta:
        db_table = "user"
        managed = False
        ordering = ['-idx']
        verbose_name        = '유저 정보'
        verbose_name_plural = '유저 정보'
    
