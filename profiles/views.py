# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    template ='home.html'
    return render(request,template,context)

def about(request):
    context={}
    template ='about.html'
    return render(request,template,context)