from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount, Transactions
from django.contrib.auth.models import User
from django import forms

class UserRegistration(UserCreationForm):
    class Meta:
        model =  User
        fields = ['username','first_name','last_name','email','password1', 'password2']

    def save(self,commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            UserAccount.objects.create(user=our_user,account_no = 100000 + our_user.id)
        return our_user
    

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount']

    def __init__(self,*args,**kwargs):
        self.account = kwargs.pop('account',None)
        super().__init__(*args,**kwargs)

    def save(self,commit=True):
        self.instance.account = self.account
        return super().save(commit=commit)
    
    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount   