from django.db import models

from mdeditor.fields import MDTextField
# Create your models here.
class Article(models.Model):
    title = models.CharField('标题',max_length=50)
    column = models.CharField('专栏',max_length=30)
    body = MDTextField()
    modified_time = models.DateTimeField(verbose_name='发布时间',auto_now=True)
    author = models.CharField('作者',max_length=20,default='admin')

    def __str__(self):
        return '%s-%s' % (self.title,self.column)