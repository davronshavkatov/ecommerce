from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    discription = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/category',blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.name
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])