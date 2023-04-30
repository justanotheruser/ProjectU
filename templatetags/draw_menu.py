from django import template

from ..models import TreeMenu, MenuNode

register = template.Library()


def node2dict(node: MenuNode):
    return {
        "text": node.text,
        "url": node.url,
        "is_selected": False
    }


def listed_tree2dict(tree_list: list[MenuNode]):
    node_dict = node2dict(tree_list[0])
    if len(tree_list) == 1:
        return node_dict
    child_depth = tree_list[0].tree_depth + 1
    subtrees = []
    subtree_list = None
    for node in tree_list[1:]:
        if node.tree_depth == child_depth:
            if subtree_list is not None:
                subtrees.append(subtree_list)
            subtree_list = [node]
        else:
            subtree_list.append(node)
    subtrees.append(subtree_list)
    node_dict['children'] = [listed_tree2dict(subtree_list) for subtree_list in subtrees]
    return node_dict


def convert_menu_for_template(root: MenuNode):
    menu_nodes = root.descendants(include_self=True)
    menu_dict = listed_tree2dict(menu_nodes)
    return menu_dict.get('children', [])


@register.inclusion_tag('menu.html')
def draw_menu(menu_name: str, url: str):
    query_set = TreeMenu.objects.filter(name=menu_name)
    if len(query_set) == 0:
        return {}
    tree_menu = query_set[0]
    return {'menu': convert_menu_for_template(tree_menu.root_node)}
