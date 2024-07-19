from django.contrib import admin
from .models import Blog



class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')

    def save_model(self, request, obj, form, change):
        if not change:  # When creating a new post
            obj.author = request.user
        obj.save()

admin.site.register(Blog, BlogAdmin)
