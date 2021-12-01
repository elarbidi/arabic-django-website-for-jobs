
# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.sitemaps import ping_google
from django.shortcuts import reverse
import sys
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
def slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    str = str.replace('"', "")
    str = str.replace("'", "")
    str = str.replace(":", "")
    return str

class les_categorie(models.Model):
    le_nom = models.CharField(max_length=250)
    def __str__(self):
        return self.le_nom

class les_ville(models.Model):
    le_nom = models.CharField(max_length=250)
    def __str__(self):
        return self.le_nom

class les_post(models.Model):
    le_nom = models.CharField(max_length=250, unique=True)
    body = RichTextUploadingField()
    sub = models.CharField(max_length=250 , null=True, blank=True)
    date_expiration = models.CharField(max_length=250 , null=True, blank=True)
    la_photo = models.ImageField( upload_to="image/")
    date  = models.DateTimeField( auto_now_add=True)
    categorie = models.ManyToManyField(les_categorie)
    villes = models.ManyToManyField(les_ville, blank=True , null=True)
    desc = models.TextField(blank=True , null=True )
    keyword = models.TextField(blank=True , null=True )
    slug = models.SlugField(blank=True , null=True)
    class Meta:
        ordering = ['-date',]
    def get_absolute_url(self):
        return reverse('article', args=[str(self.slug)])
    def save(self , force_insert=False, force_update=False):
        self.slug = slugify(self.le_nom)[:30]
        im = Image.open(self.la_photo)
        output = BytesIO()
        im = im.resize( (640,360) )
        im.save(output, format='jpeg', quality=90)
        output.seek(0)
        self.la_photo = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.la_photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super().save(force_insert, force_update)
    def __str__(self):
        return self.le_nom