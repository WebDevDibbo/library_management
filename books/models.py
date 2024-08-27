from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    


class BookModel(models.Model):
    category = models.ManyToManyField(Categories)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/media/uploads', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    

class Review(models.Model):
    post = models.ForeignKey(BookModel, related_name='review', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'Comments by {self.user.username}'