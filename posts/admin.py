from django.contrib import admin
from posts.models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "publish_date"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]  # Display comment text
   

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
