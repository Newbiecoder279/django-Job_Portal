from django.contrib import admin
from . models import PostJob

# Register your models here.


class PostJobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(PostJob, PostJobAdmin)