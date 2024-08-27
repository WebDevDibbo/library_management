from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import FormView
from . forms import UserRegistration, DepositForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Transactions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from borrow.models import BorrowModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# kjae levy stwq peae

def send_transaction_email(user,amount,subject,template):
        message = render_to_string(template,{
            'user' : user,
            'amount' : amount,
        })
        to_email = user.email
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message,'text/html')
        send_email.send()




# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    # !in UserRegistrationForm request.POST arguments are passing which cant be seen
    form_class = UserRegistration
    success_url = reverse_lazy('register')

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form) 
    # form valid funtion call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    

class UserLogoutView(LogoutView):
    # next_page =  reverse_lazy('home')
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    

class DepositView(LoginRequiredMixin,CreateView):

    template_name = 'accounts/deposit.html'
    model = Transactions
    form_class = DepositForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
        "account": self.request.user.account,
        })
        return kwargs
    

    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(update_fields = ['balance'])
        messages.success(self.request,f'{amount}$ was deposited to your account successfully')
        send_transaction_email(self.request.user,amount,"Deposit Message",'accounts/deposit_email.html')
        return super().form_valid(form)
    


class Profile(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['borrow_history'] = BorrowModel.objects.filter(user=self.request.user)
        return context

