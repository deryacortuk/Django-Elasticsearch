from PIL import Image
from io import BytesIO
from celery import shared_task
from django.core.files.base import File
from . import models
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)



@shared_task()
def create_image_thumbnail(id):
    article = models.Article.objects.get(pk=id)
    image = Image.open(article.image.path)
    SIZE = 250, 250
    image.thumbnail(SIZE, Image.LANCZOS)    
    image.save(article.image.path)
    
    