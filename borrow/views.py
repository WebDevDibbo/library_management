from django.shortcuts import render,redirect, get_object_or_404
from books.models import BookModel
from .models import BorrowModel
from accounts.models import UserAccount
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.views import send_transaction_email
# Create your views here.

def borrow(request,id):
    book_item = get_object_or_404(BookModel,pk=id)
    request_user = UserAccount.objects.get(user=request.user)
    
   
    borrow_obj = BorrowModel.objects.filter(user=request.user, book=book_item).first()
    
    if borrow_obj is None:
        if request_user.balance > book_item.price:
            request_user.balance-=book_item.price
            request_user.save()
            BorrowModel.objects.create(user=request.user, book=book_item)
            messages.success(request, 'The Book Successfully Borrowed.')
            send_transaction_email(request.user,book_item.price,"Borrow Book Message","book_buy_email.html")
            return redirect('home')
        else:
            messages.error(request,"You cant borrow this book because your balance is insufficient")
            redirect('home')
    
    else:
        messages.error(request,"This book is already borrowed")
        return redirect('home')


