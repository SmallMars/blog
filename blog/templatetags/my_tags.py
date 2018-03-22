
from django import template
register=template.Library()   #固定格式

@register.filter
def mul_filter(x,y):
    return x*y


@register.simple_tag
def mul_tag(x,y):
    return x*y

#自定义标签
from blog.models import *
@register.inclusion_tag("blog/menu.html")
def get_menu(username):
    user = UserInfo.objects.filter(username=username).first()
    blog = user.blog
    from django.db.models import Count, Max
    cate_list = Category.objects.filter(blog=blog).annotate(count=Count("article")).values_list("title", "count")
    print(cate_list)
    # 查询当前站点的每一个标签的名称以及对应的文章数：分组查询
    tag_list = Tag.objects.filter(blog=blog).annotate(count=Count("article")).values_list("title", "count")
    print(tag_list)
    # 日期归档
    date_list = Article.objects.filter(user=user).extra(
        select={"archive_date": "strftime('%%Y-%%m',create_time)"}).values("archive_date").annotate(
        c=Count("nid")).values_list("archive_date", "c")
    print(date_list)

    return {"username":username,"blog":blog,"cate_list":cate_list,"tag_list":tag_list,"date_list":date_list}




# @register.simple_tag
# def mul_tag(x,y,z):
#     return x*y*z