from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return "%d" % self.pk#priamry_key的缩写
    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def __str__(self):
        return "%d" % self.pk


