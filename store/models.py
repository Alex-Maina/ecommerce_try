from django.core.validators import MinValueValidator
from django.db import models

#promotion model
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
    def __str__(self) -> str:
        return self.description


#collection model
class Collection(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title
    

# products model
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField (default ='-')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, 
                                decimal_places=2, 
                                validators=[MinValueValidator(0)]
                                )
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ForeignKey(Promotion, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title


#customer model 
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField (max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    
    
    def __str__(self) -> str:
        return self.first_name


#Address model
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self) -> str:
        return self.title


#Order model
class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'
    
    STATUS = [ 
        (PENDING, 'Pending'),
        (COMPLETE, 'Completed'),
        (FAILED, 'Failed'),
        ]
    payment_status = models.CharField(max_length=1, choices=STATUS, default=PENDING)
    placed_at =models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
    

#Order Item Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField ()
    unit_price = models.DecimalField (max_digits=6, decimal_places=2)
    
    def __str__(self) -> str:
        return self.title


#Cart model
class Cart (models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title


#Cart Item model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        return self.title
    