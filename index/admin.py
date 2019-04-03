from django.contrib import admin
from .models import *


class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'special', 'type')  # 列表中显示的字段
    list_filter = ('type',)  # 右侧的筛选框
    search_fields = ('name', 'special', 'type')    # 上方的搜索内容


# Register your models here.
admin.site.register(User)
admin.site.register(GoodType)
admin.site.register(Good, GoodAdmin)
