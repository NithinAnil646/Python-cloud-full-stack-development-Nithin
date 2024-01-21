#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:02:26 2024

@author: nithin
"""

# msgapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.message_board, name='message_board'),
    path('submit_message/', views.submit_message, name='submit_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
]
