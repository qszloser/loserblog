from django.contrib import admin

# Register your models here.
from myblog.models import Article, Category, Tag, RotationChart


# 导入需要管理的数据库表
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表显示想要显示的字段
    list_display = ('id', 'category', 'title', 'user', 'views', 'create_time', 'update_time')
    # 满50分页
    list_per_page = 50
    # 后台数据列表排序方式
    ordering = ('-create_time',)
    # 设置那些字段可以点击进入编辑页面
    list_display_links = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index', 'img')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(RotationChart)
class RotationChartAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'img', 'create_time', 'update_time', 'is_show')
