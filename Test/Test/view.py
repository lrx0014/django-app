# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def test(request):
    context          = {}
    context['text'] = 'Test Page'
    return render(request, 'index.html', context)