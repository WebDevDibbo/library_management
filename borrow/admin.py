
from django.contrib import admin
from .models import BorrowModel

@admin.register(BorrowModel)
class BorrowModelAdmin(admin.ModelAdmin):
    list_display  = ('user', 'book', 'borrow_date', 'return_date')
    readonly_fields = ('borrow_date',)