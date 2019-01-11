from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Category(models.Model):
    categ = models.CharField('文章大类',max_length=50)

    def __str__(self):
        return self.categ

class Small_Category(models.Model):
    small_categ = models.CharField('文章小类',max_length=50)
    big_categ = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.small_categ

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField('标题',max_length=100)
    slug = models.SlugField(max_length=100,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField('内容')
    first_categ = models.ForeignKey(Category,on_delete=models.CASCADE)
    publish = models.DateTimeField('发表时间',default=timezone.now)
    created = models.DateTimeField('创建时间',auto_now_add=True)
    updated = models.DateTimeField('更新时间',auto_now=True)
    status = models.CharField('状态',max_length=10,choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])




