from django import template

from men.models import Category

register = template.Library()

@register.inclusion_tag('men/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}