from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ImageForm, PostForm, CommentForm
from .models import Post, Images, Comment
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# views handle routes to html pages, generally speaking

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)
# since we created a class based view, we dont need those lines of code anymore anyway


class PostListView(ListView):  # to display homepage with posts
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # when class view used, it is looking for a specific pattern:
    # <app>/<model>_<viewtype>.html, but we can override
    #       and also set another variable so it does not look for 'list'
    ordering = ['-date_posted']  # this would put newer ads first
    paginate_by = 10


class UserPostListView(ListView):  # to display homepage with posts
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # when class view used, it is looking for a specific pattern:
    # <app>/<model>_<viewtype>.html, but we can override
    #       and also set another variable so it does not look for 'list'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PurchaseItemView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['price', ]
    template_name = 'blog/post_purchase.html'
    success_url = reverse_lazy('blog-home')
    success_message = "Item was purchased."

    def form_valid(self, form):
        self.request.user.profile.moneys -= form.instance.price  # taking money from current user
        form.instance.author.profile.moneys += form.instance.price  # giving money to the author
        form.instance.author.profile.save()
        self.request.user.profile.save()
        form.instance.author = self.request.user  # assigning the post author to the buyer
        return super().form_valid(form)

    # self.request.user.profile.moneys is the current user (buyer) money
    # form.instance.price price of the post
    # part of mixins, blocks users from editing other user's posts
    def test_func(self):
        post = self.get_object()
        if self.request.user != post.author:
            return True
        return False


# view for each individual post
#
class PostDetailView(DetailView):  # each single post page
    model = Post


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):  # creating new post view
    model = Post
    fields = ['title', 'content', 'price', 'image']
    success_url = reverse_lazy('blog-home')
    success_message = "Post  about %(title)s was created"

    #  need to override for to set an author for the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin,
                     UpdateView):
    model = Post
    fields = ['title', 'content', 'price', 'image']
    success_url = reverse_lazy('blog-home')
    success_message = "Post  about %(title)s was updated"

    #  need to override for to set an author for the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # part of mixins, blocks users from editing other user's posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):  # each single post page
    model = Post
    success_message = "Post  about %(title)s was deleted"
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# about page, nothing here yet anyway
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def post_detail_view(request, pk):
    template_name = 'blog/comment_form.html'
    post = get_object_or_404(Post, pk=pk)
    new_comment = None

    comment_form = CommentForm(data=request.POST or None)
    if comment_form.is_valid():
        # Create Comment object but don't save to database yet
        new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
        new_comment.post = post
        # Save the comment to the database
        messages.success(request, f'Comment posted successfully!')
        new_comment.save()
        return redirect('blog-home')
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'new_comment': new_comment,
                                           'comment_form': comment_form}, )
