from django.db import models
from .utilities import BaseTimeStampModel
# Create your models here.
        
        
    
    
class Tag(BaseTimeStampModel):
    """Model definition for Tag."""

    # TODO: Define fields here
    name = models.CharField(max_length=255, null=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name
    
    





