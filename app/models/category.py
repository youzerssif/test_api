from django.db import models
from .utilities import BaseTimeStampModel

# Create your models here.



class Category(BaseTimeStampModel):
    """Model definition for Category."""

    # TODO: Define fields here
    title = models.CharField(max_length=255, null=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.title
    

    




