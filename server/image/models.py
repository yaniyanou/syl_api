#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 19:30:13 2018

@author: yanis
"""


from django.db import models
from django.core.validators import MaxLengthValidator , MinLengthValidator


class card(models.Model):
    
    