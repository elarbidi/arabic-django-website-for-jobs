from django.contrib import admin
from .models import les_ville , les_post  , les_categorie

# Register your models here.
admin.site.register(les_post)
admin.site.register(les_categorie)
admin.site.register(les_ville)