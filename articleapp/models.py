from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):    #계정 삭제 시 게시글 보존, 알수없음 표시
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/',null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True,null=True)
