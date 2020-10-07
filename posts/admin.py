from django.contrib import admin

from posts.models import Project, Category




class PostAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'title',
        'description',
        'status',
    )

admin.site.register(Project)
admin.site.register(Category)