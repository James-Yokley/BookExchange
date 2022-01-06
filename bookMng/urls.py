from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('review/', views.Review_rate, name='review'),
    path('searchbook', views.searchbook, name='searchbook'),
    path('searchresults/<str:book_name>', views.searchresults, name='searchresults'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wishlist_add/<int:book_id>', views.wishlist_add, name='wishlist_add'),
    path('wishlist_delete/<int:book_id>', views.wishlist_delete, name='wishlist_delete'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('shoppingcart_add/<int:book_id>', views.shoppingcart_add, name='shoppingcart_add'),
    path('shoppingcart_delete/<int:book_id>', views.shoppingcart_delete, name='shoppingcart_delete'),

]