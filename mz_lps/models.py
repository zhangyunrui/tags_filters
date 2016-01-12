# -*- coding: utf-8 -*-
from django.db import models


class Quiz(models.Model):
    question = models.TextField("题目描述")
    item_list = models.TextField("题目选项")
    result = models.CharField("答案", max_length=1)
    index = models.IntegerField("试题顺序(从小到大)", default=999)

    class Meta:
        verbose_name = "试卷题目"
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.question
