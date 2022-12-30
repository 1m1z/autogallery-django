from django.contrib import admin

# Register your models here.
from Blog.models import PostModel
admin.site.register(PostModel)