from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    return f'Placeholder for {menu_name}'
