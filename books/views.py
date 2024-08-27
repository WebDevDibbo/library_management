from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Review, BookModel
from .forms import ReviewForm
from borrow.models import BorrowModel


# Create your views here.
    

class CreateReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('add_review')

    def form_valid(self,form):
        return super().form_valid(form)
    

class DetailPost(DetailView):
    model = BookModel
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    context_object_name = 'book'

    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        review_form = ReviewForm(data=self.request.POST)
        post = self.get_object()
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.post = post
            new_review.user = request.user
            new_review.save()
            return redirect('book_details',id=post.id)
        return self.get(request,*args,**kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book= self.object #getting the current book

        reviews = book.review.all()
        context['reviews'] = reviews
        if self.request.user.is_authenticated:
            borrow_object = BorrowModel.objects.filter(user=self.request.user,book=book,return_date__isnull=True).first()
            review_form = ReviewForm
            if borrow_object:
                context['review_form'] = review_form()
                context['is_borrowed'] = True
            else:
                context['is_borrowed'] = False
        return context
    