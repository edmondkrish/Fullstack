from django.urls import path
from .views import home,book_list,create_book,book_detail,edit_book,delete_book
urlpatterns=[
    path('', home, name='home'),
    path('books/',book_list,name='books'),
    path('create_book/',create_book,name='create_book'),
    path('book/<int:id>/',book_detail,name='book_detail'),
    path('book/<int:id>/edit/',edit_book,name='edit_book'),
    path('book/<int:id>/delete/',delete_book,name='delete_book'),
]