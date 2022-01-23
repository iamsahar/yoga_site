from django import template
from blog.models import Category, Post

register = template.Library()


@register.simple_tag(name="posts")
def overal():
    posts = Post.objects.filter(status=1)[:3]
    return posts

@register.inclusion_tag("blog/latest-posts.html")
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by("published_date")[:arg]
    return {"posts": posts}

@register.inclusion_tag("blog/categories.html")
def postcategories(arg=3):
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories": cat_dict}
