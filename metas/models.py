from django.db import models
from meta.models import ModelMeta
import contextlib
from copy import copy
from django.conf import settings as dj_settings
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class MetasModels(ModelMeta, models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()
    video = models.FileField()
    url = models.URLField(max_length=255)

    _metadata = {
        'title': 'title',
        'og_title': 'title',
        'keywords': settings.DEFAULT_KEYWORDS,
        'og_locale': '',
        'description': 'description',
        'image': 'get_meta_image',
        'tag': 'title',
        'url': 'url',
        # 'locale': True,
        # 'object_type': True,
        # 'og_type': True,
        # 'og_app_id': True,
        # 'og_profile_id': True,
        # 'og_publisher': True,
        # 'og_author_url': True,
        # 'fb_pages': True,
        # 'twitter_type': True,
        # 'twitter_site': True,
        # 'twitter_author': True,
        # 'gplus_type': True,
        # 'gplus_author': True,
        # 'gplus_publisher': True,
        # 'published_time': True,
        # 'modified_time': True,
        # 'expiration_time': True,
    }

    def get_meta_image(self):
        if self.image:
            return self.image.url
