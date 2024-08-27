from django.contrib import admin
from .models import UserAccount, Transactions

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Transactions)