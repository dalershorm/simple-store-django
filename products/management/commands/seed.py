from django.core.management.base import BaseCommand
from products.models import Category

class Command(BaseCommand):
    help = 'Seeding Categories'

    def handle(self, *args, **options):
        
        category_list = [
            'Мужской одежды',
            'Ноутбуки',
            'Телевизоры'
        ]

        for item in category_list:
            Category.objects.create(name=item)
            print(f"Добавлен категория '{item}'")
