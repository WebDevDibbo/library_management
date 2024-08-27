
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('books/',include('books.urls')),
    path('categories/<slug:category_slug>/',home, name='category_wise_post'),
    path('borrow/', include('borrow.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
