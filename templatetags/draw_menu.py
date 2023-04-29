from django import template

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    return {'menu_name': menu_name}
