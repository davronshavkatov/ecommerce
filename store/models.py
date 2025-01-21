from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=400, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(default=100)
    is_available = models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    carated_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
