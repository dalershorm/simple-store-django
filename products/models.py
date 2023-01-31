from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    STATUS_CHOICES = (
        ("active", "Актиный" ),
        ("deactive", "Не актиный"),
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='categories/%Y/%m/%d', null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='active')
    show_in_home = models.CharField(max_length=100, choices=STATUS_CHOICES, default='active')

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    STATUS_CHOICES = (
        ("active", "Актиный" ),
        ("deactive", "Не актиный"),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10000, decimal_places=0)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='active')
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name


