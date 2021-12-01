from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import les_post
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index','tawjih','anapec','stage','talaba','jobs','teq']
    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
    def items(self):
        return les_post.objects.filter().order_by('-date')[:1000]
    def lastmod(self, obj):
        return obj.date