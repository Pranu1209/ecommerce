from django.db import models
from categories.models import Category
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.


class Product(models.Model):
    """
    Product Model class
    """

    class Meta:
        ordering = ("-created",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    product_code = models.CharField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacture_date = models.DateTimeField(auto_now_add = True)
    expires_date = models.DateTimeField(auto_now=True, editable=False)
    owner = models.ForeignKey(User)
    status = models.CharField(max_length=100, (choices = choices) default="In Progress")
choices = (('Received','Received'),
           ('Scheduled','Scheduled'),
           ('Shipped','Shipped'),
           ('In Progress','In Progress'),
           )
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.slug})

