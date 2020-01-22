# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import Avg


class Ratings(models.Model):
    movie_name = models.TextField()
    ratings = models.IntegerField()

