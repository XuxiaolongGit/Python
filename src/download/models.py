from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField('书名',max_length=50)
    size = models.CharField('大小',default='未知',max_length=20)
    c_time = models.DateTimeField(verbose_name='上传时间',auto_now_add=True)
    uploader = models.CharField('上传者',max_length=20,default='admin')

    def __str__(self):
        return '%s-%s' % (self.name,self.size)
