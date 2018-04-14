#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:28:10 2018

@author: yanis
"""

from django.db import models
from django.core.validators import MaxLengthValidator , MinLengthValidator



class Ouruser(models.Model):
    
    #MinLength allow us to refuse the non value
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    surname = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    email = models.EmailField()
    
    #We represente the user who create the account