from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    STATUS_CHOICES = (
        ("Актиный", "active"),
        ("Не актиный", "deactive"),
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='categories/%Y/%m/%d')
    status = models.CharField(choices=STATUS_CHOICES, default='active')
    show_in_home = models.CharField(choices=STATUS_CHOICES, default='active')

    def slug(self):
        return slugify(self.slug)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    STATUS_CHOICES = (
        ("Актиный", "active"),
        ("Не актиный", "deactive"),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(default=1.0)
    status = models.CharField(choices=STATUS_CHOICES, default='active')
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.slug)

    def __str__(self):
        return self.name
    







