from django.db import models
from PIL import Image
from users.models import Customer

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

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        # this property prevents from getting error on page if image doesn't exist
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 750 or img.width > 750:
            output_size = (750, 750)    # max size in pixels for uploaded image
            img.thumbnail(output_size)  # we make thumbnail of image in given shape
            img.save(self.image.path)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    # if customer is deleted set the null value for customer field
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        orderitems = self.orderitem_set.all()
        return sum([item.total_price for item in orderitems])
    
    @property
    def items_counter(self):
        orderitems = self.orderitem_set.all()
        return sum([item.quantity for item in orderitems])
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product.price * self.quantity

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address