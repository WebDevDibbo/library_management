from django.db import models
from django.contrib.auth.models import User
from books.models import BookModel
from accounts.models import UserAccount

# Create your models here.
class BorrowModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return str(self.borrow_date)