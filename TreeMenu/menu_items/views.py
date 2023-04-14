from django.views.generic import ListView

from .models import MenuItem


class MenuItemView(ListView):
    model = MenuItem
    template_name = 'menu_items/index.html'
