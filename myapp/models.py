from django.db import models

# Create your models here.
class Control(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    img_url=models.URLField(null=True)
    def __str__(self):
        return self.title


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    perfume_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name} - {self.perfume_name}"
