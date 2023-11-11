from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField

# Create your models here.
class BlogPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    api_fields = [
        APIField('intro'),
        APIField('body'),
    ]


