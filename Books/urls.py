from django.urls import path
from Books import  views 

urlpatterns = [
   
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<str:pk>', views.book_update, name='book_update'),
    path('books/delete/<str:pk>/', views.book_delete, name='book_delete'),
]