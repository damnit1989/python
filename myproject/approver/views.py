# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
# from django.views.generic.simple import direct_to_template
from myproject import settings
from poster.views import *
from poster.models import Tweet, Comment

# Create your views here.

def list_tweets(request):
    twees_list = {}
    twees_list['pending_tweets'] = Tweet.objects.filter(state = 'pending').order_by('created_at')
    twees_list['published_tweets'] = Tweet.objects.filter(state = 'published').order_by('-published_at')
    return render(request,'list_tweets.html',twees_list)