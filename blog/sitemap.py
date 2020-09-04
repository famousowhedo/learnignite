from django.contrib.sitemaps import Sitemap
from .models import Course


class MyCOurseSiteMap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Course.objects.all()

    def location(self, item):
        return '/home/' +str(item)    

