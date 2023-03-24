from django.db import models
from PIL import Image

# Create your models here.
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    CATEGORIES = (
        ('Hats', 'Hats'),
        ('Jacket', 'Jacket'),
        ('Trousers', 'Trousers'),
        ('Shoes', 'Shoes'),
        ('Sweatshirt', 'Sweatshirt'),
    )
    name = models.CharField(max_length=100, default='Product')
    image = models.ImageField(upload_to='product_pics')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=1, choices=SIZES)
    color = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORIES)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 750 or img.width > 750:
            output_size = (750, 750)    # max size in pixels for uploaded image
            img.thumbnail(output_size)  # we make thumbnail of image in given shape
            img.save(self.image.path)
