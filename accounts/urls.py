from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name = 'register'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('deposit/',views.DepositView.as_view(), name='deposit'),
    path('profile/',views.Profile.as_view(),name='profile'),
]
