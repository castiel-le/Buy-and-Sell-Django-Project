from django import forms
from .models import Post, Images, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    text = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'content')
