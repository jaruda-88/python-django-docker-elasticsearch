from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from elasticsearch_dsl import connections, Q


def search(request)
# class ArticleView(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

    # def get_queryset(self):
    #     title = self.request.query_params.get("title")
    #     category = self.request.query_params.get("category")

    #     query = Q()

    #     if title:
    #         query &= Q(title=title)
    #     if category:
    #         query &= Q(category=category)
        
    #     queryset = Article.objects.filter(query)

    #     return queryset

