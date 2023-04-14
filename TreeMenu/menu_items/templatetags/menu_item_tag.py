from menu_items.models import MenuItem
from django import template

register = template.Library()


@register.simple_tag()
def get_menu(path):
    result = MenuItem.objects \
        .select_related('parent') \
        .filter(posting_link=path, parent=None) \
        .prefetch_related('childs') \
        .prefetch_related('childs')

    return result
