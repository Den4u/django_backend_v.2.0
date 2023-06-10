from django.contrib import admin

from .models import Post, Location, Category


admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Category)
