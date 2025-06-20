from django.urls import path
from .import views

urlpatterns = [
    path("",views.StartingPageView.as_view(),name='starting_page'),
    path("posts",views.AllPostsView.as_view(),name='posts'),
    path("posts/<int:pk>",views.SinglePostView.as_view(),name='post_detail'),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]
