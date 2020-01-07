# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 22:52:38
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-04-24 03:37:47
from rest_framework import viewsets, filters
from .models import Article
from .serializers import ArticleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class ArticleViewSet(viewsets.ModelViewSet):
	# permission_classes = (IsAuthenticated,)
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('article_id', 'article_heading', 'article_body')
