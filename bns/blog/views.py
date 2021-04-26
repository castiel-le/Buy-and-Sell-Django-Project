from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin


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


# view for each individual post
#
class PostDetailView(DetailView):  # each single post page
    model = Post


class PostCreateView(SuccessMessageMixin, CreateView):  # creating new post view
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog-home')
    success_message = "Post  about %(title)s was created"

    #  need to override for to set an author for the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# about page, nothing here yet anyway
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
