from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet, ArticleDocumentViewSet, ArticleSearch,ArticleRetriveUpdateDestroy

router = routers.DefaultRouter()

router.register(r'articles', ArticleViewSet)
router.register(r'article-document',ArticleDocumentViewSet,basename="article-document")


urlpatterns = [
     path('', include(router.urls)),
     path("search/<str:query>/", ArticleSearch.as_view()),    
     path('article/<id>/',ArticleRetriveUpdateDestroy.as_view())
]
