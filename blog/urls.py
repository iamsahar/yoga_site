from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('search/', blog_search, name='search'),
]
