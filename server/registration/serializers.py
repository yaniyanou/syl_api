#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:35:25 2018

@author: yanis
"""

from rest_framework import serializers
from registration.models import Ouruser 


class OuruserSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Ouruser
        fields = ("id", "name", "surname", "email")
