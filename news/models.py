import imp
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import MultiFieldPanel, InlinePanel, FieldPanel, PageChooserPanel
from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.images.api.fields import	 ImageRenditionField
class HomePageCarouselImages(Orderable):
    page = ParentalKey("news.NewsPage",related_name="carousel_images")
    carousel_title = models.CharField(max_length = 150,null=True,blank=True)
    carousel_subtitle= models.CharField(max_length = 150,null=True,blank=True)
    carousel_cta= models.URLField(null=True,blank=True)
    
    carousel_image=models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels=[
        ImageChooserPanel("carousel_image"),
        FieldPanel('carousel_title'),
        FieldPanel('carousel_subtitle'),
        FieldPanel('carousel_cta'),

    ]
    api_fields=[
        APIField("carousel_image_t",serializer=ImageRenditionField("fill-2000x500",source='carousel_image')),
        APIField("carousel_title"),
        APIField("carousel_subtitle"),
        APIField("carousel_cta"),
    ]
class NewsPage(Page):
    intro = models.CharField(max_length=50)
    body=RichTextField(blank=True)
    content_panels=Page.content_panels+[
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("carousel_images",max_num=5,min_num=1,label="Image"),

    ]
    api_fields=[
        APIField("intro"),
        APIField("title"),
        APIField("body"),
        APIField("carousel_images"),

    ]