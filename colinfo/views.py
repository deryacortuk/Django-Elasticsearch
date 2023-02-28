from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Article
from elasticsearch_dsl import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    SUGGESTER_COMPLETION,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .serializers import ArticleSerializer, ArticleDocumentSerializer
from .documents import ArticleDocument
from rest_framework import generics

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
  
    

    
class ArticleRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        return serializer.save()
    def get_queryset(self):
        return self.queryset.filter()

class ArticleSearch(APIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q('multi_match', query=query,
                 fields=[
                    'title',
                    'content',
                    'author.username',
                ], fuzziness='auto')

    def get(self, request, query):
        q = self.generate_q_expression(query)
        search = self.document_class.search().query(q)
        return Response(self.serializer_class(search.to_queryset(), many=True).data)

class ArticleDocumentViewSet(DocumentViewSet):
    serializer_class = ArticleDocumentSerializer
    document = ArticleDocument
    
    ordering = ('id',)
    lookup_field = 'id'

    filter_backends = (
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    )

    search_fields = (
        'title',
        'content',
        'author'
    )

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,               
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
       
    }

    suggester_fields = {
        'title': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
    
    
    # class ArticleCreate(generics.CreateAPIView):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
    
#     def create(self, request, *args, **kwargs):
#         return super(ArticleCreate, self).create(request, *args, **kwargs)