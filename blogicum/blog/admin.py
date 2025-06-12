from django.contrib import admin
from .models import Post, Category, Location, Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Comment)