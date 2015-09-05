from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class NewsPost(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(_('title'), max_length=256)
    body = models.TextField(_('body'), )
    timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)
    
    def __unicode__(self):
        return self.title