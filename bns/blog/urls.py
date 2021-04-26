from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

# .as_view for class based views
# use variables for single post views!
# detailView expects 'pk' in the variables
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]


# when class view used, it is looking for a specific pattern:
# <app>/<model>_<viewtype>.html, so in our case that would be blog/