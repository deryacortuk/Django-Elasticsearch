from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# from django.contrib.sites.shortcuts import get_current_site
# from .utils import get_current_site
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
import os
from datetime import datetime
from . import tasks

def article_directory_path(instance, filename):
    
    article_img_name = 'article_{0}/slug_{1}/article.jpg'.format(instance.author.id,instance.slug)    
    return article_img_name

class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager,self).get_queryset().filter(status = 'P')

class Article(models.Model):
    STATUS_CHOICES = (
        ('D', 'DRAFTED'),
        ('P', 'PUBLISHED'),
    )
    author = models.ForeignKey(User, verbose_name="author",blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    published_time = models.DateTimeField(blank=False, null=False, default=now)
    status = models.CharField(choices=STATUS_CHOICES, default='D',max_length=100)
    image = models.ImageField(upload_to=article_directory_path,blank = True, null= True, verbose_name='image')    
    
    objects = models.Manager()
    published = PublishManager()    
    
    class Meta:
        ordering = [ '-published_time']
        verbose_name = "article"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        
        if self.image:
            tasks.create_image_thumbnail.delay(self.pk)
        super(Article, self).save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("model:detail", args=[self.slug])
    
    
    
    # def get_full_url(self):
    #     site = get_current_site().domain
    #     url = "https://{site}{path}".format(site=site,path=self.get_absolute_url())
    #     return url
    

    # def indexing(self):
    #     obj = ArticleIndex(
    #         meta={'id': self.id},
    #         author=self.author.username,    #               
    #         title=self.title,          
    #         created_time=self.created_time,
    #         published_time=self.publihsed_time,
    #     )
    #     obj.save()
    #     return obj.to_dict(include_meta=True)
 
    
