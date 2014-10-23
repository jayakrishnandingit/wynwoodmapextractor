# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from artist.models import Artist


class ArtistItem(DjangoItem):
    # define the fields for your item here like:
    django_model = Artist
