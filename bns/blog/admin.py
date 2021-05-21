from django.contrib import admin

from .models import Post, Images, Comment


class PostImageAdmin(admin.StackedInline):
    model = Images


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(Images)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'content')

