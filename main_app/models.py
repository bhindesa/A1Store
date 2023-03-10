from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('F','Furniture'),
    ('T','Toy'),
    ('C','Cloth'),
    ('M','Mobile Phone'),
    ('L','Laptop'),
)



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    category =  models.CharField(
            max_length=1,
            # add the 'choices' field option
            choices=CATEGORY,
            # set the default value for meal to be 'B'
            default=CATEGORY[0][0]
        )
    
    class Meta:
        ordering = ['-price']

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f' product name : {self.name}, Category :{self.get_category_display()}, Price : {self.price}'
    
    def get_absolute_url(self):
        return reverse('main_app:detail', kwargs={'prod_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
         
        return f"Photo for cat_id: {self.product_id} @{self.url}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =  models.IntegerField(default=1)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f'{self.id}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)

    def __str__(self):
        return str(self.product_id);


