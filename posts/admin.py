from django.contrib import admin

from posts.models import Project



admin.site.register(Project)
class PostAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'title',
        'description',
        'status',
    )
