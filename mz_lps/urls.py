# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^tag/$', "mz_lps.views.tag", name="tag"),
                       url(r'^filter/$', "mz_lps.views.filter", name="filter"),
                       url(r'^(?P<name>\w+)/(?P<age>\d+)/$', "mz_lps.views.name_age", name="name_age"),
                       )





