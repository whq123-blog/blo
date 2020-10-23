from django.shortcuts import render
from .models import BookInfo
# Create your views here.
def index(request):
    booklist = BookInfo.objects.all()#书数据列表------V与模型M建立联系
    return render(request,'booktest/index.html',{'booklist':booklist})
    #render(请求对象,'模板位置',传的数据字典类型)-------V与模板T建立联系
def detail(request,id):
    book = BookInfo.objects.get(pk=id)
    return render(request,'booktest/detail.html',{'book': book})



