from .models import Article
from django_elasticsearch_dsl import Document, fields
from django.contrib.auth.models import User
from django_elasticsearch_dsl.registries import registry


        
@registry.register_document
class ArticleDocument(Document):
    
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),             
        'username': fields.TextField(),
    })
    
    class Index:
        name = "articles"
        settings = {
           'number_of_shards': 1,
            'number_of_replicas': 0,
        }
        
    class Django:
        model = Article
        fields = ["title","content", "published_time"]
            
        

