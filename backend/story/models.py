from datetime import datetime
from django.db import models

class Story(models.Model):
    idx = models.AutoField(primary_key=True, verbose_name="게시글 ID")
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="게시판 명")
    content = models.CharField(max_length=200, null=False, blank=False, verbose_name="본문")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    update_date = models.DateTimeField(auto_now=True, verbose_name="수정시간")
    views = models.IntegerField(verbose_name="조회수")
    comments = models.IntegerField(verbose_name="댓글수")

    class Meta:
        db_table = "story"
        managed = False
        ordering = ['-idx']
        
    def __str__(self):
        return self.title
    
    @property
    def update_view(self):
        self.views = self.views + 1
        self.save()
    
          
