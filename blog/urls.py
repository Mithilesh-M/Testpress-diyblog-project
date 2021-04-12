from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blogs/<int:pk>/comment/', views.Comment_blog, name='comment'),
    path('blog/create/', views.CreateBlog, name='create-blog'),
    path('blog/<int:pk>/delete', views.PostDelete, name='post-delete'),
    path('blogger/<int:pk>/delete', views.BloggerDelete, name='blogger-delete'),
    path('blogger/create/', views.CreateBlogger, name='create-blogger'),
    path('blogger/<int:pk>/update', views.BloggerUpdate, name='blogger-update'),
    path('blog/<int:pk>/update', views.PostUpdate, name='post-update'),
]
