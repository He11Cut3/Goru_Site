from django import template
from shop.models import Category, Product

register = template.Library()

def get_all_categories():
    return Category.objects.all()

@register.simple_tag()
def get_list_category():
    return get_all_categories()

@register.inclusion_tag('top/top_nav.html')
def get_categories():
    category = get_all_categories()
    return{"list_category" : category}

@register.inclusion_tag('top/top_nav_last.html')
def get_last_product():
    product = Product.objects.select_related("category").order_by("-id")[:2]
    return{"list_last_product" : product}