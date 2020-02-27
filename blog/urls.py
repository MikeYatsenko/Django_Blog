from django.urls import path
from . import views

urlpatterns = [
       path("about/", views.AboutView.as_view(), name="about"),
       path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
       path("", views.PostListView.as_view(), name='post_list'),
       path("post/new", views.CreatePostView.as_view(), name="post_new"),
       path("post/<int:pk>/edit", views.UpdatePostView.as_view(), name="update"),
       path("post/<int:pk>/delete", views.PostDeleteView.as_view, name="delete"),
       path("drafts/", views.DraftListView.as_view(), name="drafts"),
       path("post/<int:pk>/comment", views.add_comment_to_post, name="add_comment_to_post"),
       path("post/<int:pk>/approve", views.comment_approve, name ="comment_approve"),
       path("post/<int:pk>/remove", views.comment_remove, name="comment_remove"),
       path("post/<int:pk>/publish", views.post_publish, name="publish")
]