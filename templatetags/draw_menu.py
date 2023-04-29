from django import template

from ..models import TreeMenu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    query_set = TreeMenu.objects.filter(name=menu_name)
    if len(query_set) == 0:
        return {}
    tree_menu = query_set[0]
    menu_nodes = tree_menu.root_node.descendants(include_self=True)
    # return {'menu_nodes': menu_nodes}
    return {
        "menu": [{
            "text": "Напитки",
            "url": "/drinks",
            "is_selected": True,
            "children": [
                {
                    "text": "Кофе",
                    "url": "/drinks/coffee",
                },
                {
                    "text": "Чай",
                    "url": "/drinks/tea",
                    "is_selected": True,
                    "children": [
                        {
                            "text": "Зелёный",
                            "url": "/drinks/tea/green"
                        },
                        {
                            "text": "Чёрный",
                            "url": "/drinks/tea/black"
                        }
                    ]
                }
            ]
        }]
    }
