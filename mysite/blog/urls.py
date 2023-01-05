from django.urls import path
from . import views

urlpatterns = [
    #posts
    path('', views.post_list, name='post_list'),
    path('<int:post_id>', views.post_detail, name='post_detail'),#show all comments
    path('new', views.new_post, name='new_post'),
    path('<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete', views.delete_post, name='delete_post'),
    #comments
    path('<int:post_id>/new_comment', views.new_comment, name='new_comment'),
    path('<int:post_id>/comment/<int:comment_id>/edit', views.edit_comment, name='edit_comment'),
    path('<int:post_id>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    #likes
    #path('<int:post_id>/new_like', views.new_like, name='new_like'),
]