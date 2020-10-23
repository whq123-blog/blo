from django.contrib import admin
#from models import BookInfo python 2.7写法
from .models import BookInfo,HeroInfo
# Register your models here.
#管理员页面、普通页面显示
class QuestionAdmin(admin.ModelAdmin):
    ...



class HeroInfoInline(admin.TabularInline):
    model = HeroInfo#?
    extra = 2#?

class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]#中括号对象?
    list_display = ['pk', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    # fields = ['bpub_date', 'btitle']
    fieldsets = [
        ('basic', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),
    ]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','gender','hcontent']

admin.site.register(BookInfo,BookInfoAdmin)

