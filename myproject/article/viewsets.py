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


from django.http import HttpResponse  
from myproject import settings  
from django.core.mail import send_mail  
from django.template.loader import render_to_string

def mail(request):  
    subject = "Greetings"
    image_url ="https://www.qries.com/images/banner_logo.png"
    html_message = render_to_string(
            'htm_file.html',
            {
                'message': 'Congratulations for your success ',
                'image_url':image_url,
                }
        )
    # msg     = "Congratulations for your success"  
    to      = "kesava@asareri.com"  
    res     = send_mail(subject,html_message, settings.EMAIL_HOST_USER, [to], html_message=html_message)
    
    if(res == 1):  
        msg = "<span style='color:green'>Mail Sent Successfuly</span>"  
    else:  
        msg = "<span style='color:red'>Mail could not sent</span>"  
    return HttpResponse(msg) 


class ArticleViewSet(viewsets.ModelViewSet):
	
	# permission_classes = (IsAuthenticated,)
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('article_id', 'article_heading', 'article_body')
