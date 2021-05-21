from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, \
    PurchaseItemView
from . import views

# .as_view for class based views
# use variables for single post views!
# detailView expects 'pk' in the variables
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/comment', views.post_detail_view, name='post-comment'),
    path('post/<int:pk>/purchase', PurchaseItemView.as_view(), name='post-purchase'),
]


# when class view used, it is looking for a specific pattern:
# <app>/<model>_<viewtype>.html, so in our case that would be blog/