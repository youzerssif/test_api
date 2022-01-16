from django.db import models
from django.contrib.auth.models import User

from .utilities import BaseTimeStampModel
from .category import Category
from .tag import Tag

# Create your models here.
    
    
class Article(BaseTimeStampModel):
    """Model definition for Article.""" 

    # TODO: Define fields here
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.title
    




