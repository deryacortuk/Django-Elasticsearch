from rest_framework import serializers
from .models import Article
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import ArticleDocument

class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument
        fields = ("id","title","content", "author")
        
class ArticleSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Article
        fields = ("title", "content", "author","image","published_time")