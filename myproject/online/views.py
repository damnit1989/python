# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from poster.models import User
# Create your views here.

def index(request):
    return HttpResponse('首页!')     