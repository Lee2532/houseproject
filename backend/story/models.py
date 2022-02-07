from datetime import datetime
from django.db import models

class Story(models.Model):
    idx = models.AutoField(primary_key=True, verbose_name="게시글 ID")
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="게시판 명")
    content = models.CharField(max_length=200, null=False, blank=False, verbose_name="본문")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    update_date = models.DateTimeField(auto_now=True, verbose_name="수정시간")
    views = models.IntegerField(verbose_name="조회수", blank=True, default=0)
    comments = models.IntegerField(verbose_name="댓글수", blank=True, default=0)

    class Meta:
        db_table = "story"
        managed = False
        ordering = ['-idx']
        verbose_name        = '게시판'
        verbose_name_plural = '게시판'
        
    def __str__(self):
        return self.title
    
class StoryComment(models.Model):
    story_idx = models.ForeignKey(Story, verbose_name="게시판_번호", on_delete=models.CASCADE, db_column="story_idx")
    idx = models.AutoField(primary_key=True, verbose_name="게시판 댓글 idx")
    author = models.CharField(max_length=20, null=False)
    content = models.CharField(max_length=100, null=False)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    update_date = models.DateTimeField(auto_now=True, verbose_name="수정시간")
    
    class Meta:
            db_table = "story_comment"
            managed = False
