from csv import DictWriter

from cats.models import Cat
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates csv report'

    def handle(self, *args, **options):
        with open('log.csv', 'w', newline='') as csvfile:
            fieldnames = ['preys_number', 'name']
            writer = DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for cat in Cat.objects.get_queryset():
                writer.writerow({'preys_number': cat.get_prays_number(), 'name': cat.name})
