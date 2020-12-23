from django.db import models
from django.contrib.auth.models import AbstractUser
from mdeditor.fields import MDTextField
from PIL import Image


# Create your models here.
# 实体类

# 用户
class User(AbstractUser):
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 分类
class Category(models.Model):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=1, verbose_name='分类排序')
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    digest = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    body = MDTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveBigIntegerField('阅读量', default=0)
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 轮播图
class RotationChart(models.Model):
    img = models.ImageField(upload_to='rotation_chart/%Y/%m/%d/', verbose_name='轮播图图片')
    title = models.CharField('轮播图标题', max_length=70)
    content = models.TextField('轮播图文本', max_length=200, blank=True, null=True)
    is_active = models.BooleanField('是否是activity', default=False)
    is_show = models.BooleanField('是否展示', default=True)
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        super(RotationChart, self).save()
        image = Image.open(self.img)
        image = image.resize((960, 540), Image.ANTIALIAS)
        image.save(self.img.path);

    def __str__(self):
        return self.title
