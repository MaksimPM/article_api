import os

from django.core.management import BaseCommand

from catalog.models import Category, Article


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Article.objects.all().delete()
        #return os.system('python3 manage.py dumpdata > catalog.json')
