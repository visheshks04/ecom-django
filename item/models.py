from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, default="Uncategorised")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"


class Item(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('name', 'price')