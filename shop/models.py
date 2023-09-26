from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/products/", height_field="image_height", width_field="image_width", max_length=255)
    image_height = models.PositiveIntegerField(editable=True, null=True)
    image_width = models.PositiveIntegerField(editable=True, null=True)
    
    def __str__(self):
        return self.name
