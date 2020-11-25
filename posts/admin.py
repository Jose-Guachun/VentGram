from django.contrib import admin

from posts.models import Project, Category, Status, TypeProject




class PostAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'title',
        'description',
        'status',
    )

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(TypeProject)
admin.site.register(Status)