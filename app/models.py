from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator,MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
from joblib import load
User=get_user_model()
STATE_CHOICES=(
    ('Barisal Division','Barisal Division'),
    ('Chittagong Division','Chittagong Division'),
    ('Dhaka Division','Dhaka Division'),
    ('Mymendingh Division','Mymendingh Division'),
    ('Khulna Division','Khulna Division'),
    ('Rajshahi Division','Rajshahi Division'),
    ('Rangpur Division','Rangpur Division'),
    ('Sylhet Division','Sylhet Division'),
)
class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality= models.CharField(max_length=200)
    city= models.CharField(max_length=50)
    zipcode= models.IntegerField()
    state= models.CharField(choices=STATE_CHOICES,max_length=50)
    
    def __str__(self):
        return str(self.id)
    


CATAGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    quantity=models.IntegerField(null=True,blank=True,default=5)
    colour=models.CharField(max_length=20,null=True,blank=True)
    size=models.CharField(max_length=20,null=True,blank=True)
    catagory=models.CharField(choices=CATAGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')
    # predicted_price = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

# class PricePredictionInput(models.Model):
#     ram = models.IntegerField()
#     rom = models.IntegerField()


# class data(models.Model):
#     ram=models.FloatField()
#     rom=models.FloatField()
#     predictions=models.FloatField(blank=True)
#     def save(self, *args, **kwargs):
#         ml_model = joblib.load('predict.joblib')
#         self.predictions = ml_model.predict(
#             [[self.ram, self.rom, self.price]])
#         return super().save(*args, *kwargs)   
#     def __str__(self):
#         return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class Orderplaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price