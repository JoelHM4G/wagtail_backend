from tabnanny import verbose
from django.db import models
from wagtail.api import APIField


class Religion(models.Model):
    name = models.CharField(max_length=50)
    api_fields=[
        APIField("name"),
    ]
    
    def __str__(self):
        return self.name

class Hobbies(models.Model):
    name = models.CharField(max_length=50)
    api_fields=[
        APIField("name"),
    ]
    
    def __str__(self):
        return self.name
  

class Subscribers(models.Model):
    email=models.CharField(max_length=100,blank=True,null=False,help_text="Email Address")
    full_name=models.CharField(max_length=100,blank=False,null=False,help_text="First Name")
    religion=models.ForeignKey(Religion,on_delete=models.CASCADE,null=True,blank=True)
    hobbies = models.ManyToManyField(Hobbies)

    api_fields=[
        APIField("email"),
        APIField("full_name"),
        APIField("religion"),
    ]
    
    def __str__(self):
        return self.full_name
    def getHobbies(obj):
        return "\n,".join([p.name for p in obj.hobbies.all()])
    class Meta:
        verbose_name="Subscriber"
        verbose_name_plural="Subscribers"