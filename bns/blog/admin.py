from django.contrib import admin

from .models import Post, Images


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
