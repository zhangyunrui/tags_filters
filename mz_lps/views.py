# -*- coding: utf-8 -*-
from django.http.response import HttpResponse

from django.shortcuts import render

from models import Quiz


def tag(request):
    quizs = Quiz.objects.all().values('item_list', 'result')[:8]
    quiz = Quiz.objects.all().values('item_list', 'result', 'index')[:1][0]
    return render(request, 'tag.html', locals())


def name_age(request, age, name):
    return HttpResponse(str(name) + ' is ' + str(age))


def filter(request):
    quizs = Quiz.objects.all().values('item_list', 'result')[:8]
    quiz = Quiz.objects.all().values('item_list', 'result', 'index')[:1][0]
    return render(request, 'filter.html', locals())
