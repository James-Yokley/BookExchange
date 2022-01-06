from django.contrib import admin

# Register your models here.

from .models import MainMenu
from .models import Book, Review, Wishlist, Search, Shoppingcart


admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Wishlist)
admin.site.register(Search)
admin.site.register(Shoppingcart)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'book', 'rating',  'created_at']
    readonly_fields = ['created_at']
