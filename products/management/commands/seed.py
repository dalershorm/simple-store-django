from django.core.management.base import BaseCommand
from products.models import Category
import requests

class Command(BaseCommand):
    help = 'Seeding Categories'

    def handle(self, *args, **options):

        r = requests.get('https://qxtl5byxyj.execute-api.eu-central-1.amazonaws.com/prod/service_setting/widgets?city_id=1&widget_types=menu')
        data = r.json()
        print(data['response'][0]['widget_items'])
        
        # category_list = [
        #     'Мужской одежды',
        #     'Ноутбуки',
        #     'Телевизоры'
        # ]

        for item in data['response'][0]['widget_items']:
            Category.objects.create(name=item['label'])
            print(f"Добавлен категория '{item['label']}'")

            if len(item['child']) > 0:
                for sun_item in item['child']:
                    Category.objects.create(name=sun_item['label'])
                    print(f"Добавлен категория '{sun_item['label']}'")




