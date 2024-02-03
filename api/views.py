from rest_framework import viewsets, generics

from articles.models import Article
from .serializers import ArticleSerializer

class ArticleList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) FOr view based permission
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (IsAuthororReadOnly,)
    queryset=Article.objects.all()
    serializer_class = ArticleSerializer