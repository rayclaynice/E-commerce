from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 250, db_index = True)
    slug = models.SlugField(max_length=250, unique= True)




    class Meta:
        verbose_name_plural ='categories'


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
          return reverse('category_details', args=[self.slug])
    


class Product(models.Model):
    title = models.CharField(max_length = 250)
    brand = models.SlugField(max_length=250, default= 'unbranded')
    description = models.TextField(blank= True)
    slug = models.SlugField(max_length = 255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = ResizedImageField(size=[750,800 ], crop=['middle', 'center'], upload_to ='images/')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)



    class Meta:
        verbose_name_plural ='products'


    def __str__(self):
        return self.title
    


    def get_absolute_url(self):
          return reverse('product_details', args=[self.slug])
    

    #kwargs={'pk':self.pk, 'slug':self.slug}