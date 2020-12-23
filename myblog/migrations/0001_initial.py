# encoding: utf-8
"""
@author: qsz
@contact: qsz2961914151@gmail.com
@time: 2020/12/21 下午11:54
@file: 0001_initial
@desc: 
"""
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('auth','0011_update_proxy_permissions'),
    ]
    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
                ),
                ('name',models.CharField(max_length=100,verbose_name='博客分类')),
                ('index',models.IntegerField(default=1,verbose_name='分类排序')),
                ('img',models.ImageField(upload_to='article_img/%Y/%m/%d/',verbose_name='文章图片')),

            ],
            options={
                'verbose_name':'博客分类',
                'verbose_name_plural':'博客分类',
            },
        ),
        migrations.CreateModel(
            name='RotationChart',
            fields=[
                ('id',models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('img',models.ImageField(upload_to='rotation_chart/%Y/%m/%d/')),
                ('title',models.CharField(max_length=70,verbose_name='轮播图标题')),
                ('content',models.TextField(blank=True,max_length=200,null=True,verbose_name='轮播图文本')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否是active')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True,
                                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                              verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('digest', models.TextField(blank=True, max_length=200, verbose_name='摘要')),
                ('body', mdeditor.fields.MDTextField()),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                               to='myblog.Category', verbose_name='分类')),
                ('tag', models.ManyToManyField(blank=True, to='myblog.Tag', verbose_name='标签')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                           verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
