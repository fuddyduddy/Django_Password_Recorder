from django.contrib import admin

from .models import User, AuthLevel, Account

# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('lastName' ,'firstName','email','password','auth')
    list_filter = ('email','auth')

admin.site.register(AuthLevel)

# admin.site.register(Account)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ['accountName','summary','userID','email','password','auth',('date_of_created','date_of_deleted')]
    # fieldsets = (
    #     (None, {
    #         ('accountName','summary','userID','email','password','auth')
    #     }),
    #     ('Dates', {
    #         ('date_of_created','date_of_deleted')
    #     })
    # )

# # Inline editing of associated records
# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inlines = [BooksInstanceInline]