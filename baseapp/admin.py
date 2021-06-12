from django.contrib import admin
from baseapp.models import Post,Comment
from .models import Category



admin.site.register(Comment)
admin.site.register(Category)

from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    list_display  = ('writer', 'title', 'post_date','category')
    list_filter = ('writer', 'title',)
    # search_fields = ['writer',]



admin.site.register(Post, AuthorAdmin)
