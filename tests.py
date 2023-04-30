from django.test import TestCase

from .models import MenuNode
from .templatetags.draw_menu import listed_tree2dict


class ListedTree2DictTest(TestCase):
    def test_root_only(self):
        root = MenuNode.objects.create(url='root', is_named_url=False, text='root')
        result = listed_tree2dict(root.descendants(include_self=True))
        self.assertEqual({'text': 'root', 'url': 'root', 'is_selected': False}, result)

    def test_one_level_one_child(self):
        root = MenuNode.objects.create(url='root', is_named_url=False, text='root')
        ch1 = MenuNode.objects.create(parent=root, url='some url', is_named_url=False, text='some text')
        result = listed_tree2dict(root.descendants(include_self=True))
        self.assertEqual({'text': 'root', 'url': 'root', 'is_selected': False,
                          'children': [{'text': 'some text', 'url': 'some url', 'is_selected': False}]}, result)

    def test_one_level_multiple_children(self):
        root = MenuNode.objects.create(url='root', is_named_url=False, text='root')
        ch1 = MenuNode.objects.create(parent=root, url='one', is_named_url=False, text='one')
        ch2 = MenuNode.objects.create(parent=root, url='two', is_named_url=False, text='two')
        result = listed_tree2dict(root.descendants(include_self=True))
        self.assertEqual({'text': 'root', 'url': 'root', 'is_selected': False,
                          'children': [
                              {'url': 'one', 'text': 'one', 'is_selected': False},
                              {'url': 'two', 'text': 'two', 'is_selected': False}]}, result)

    def test_three_levels(self):
        root = MenuNode.objects.create(url='root', is_named_url=False, text='root')
        ch1 = MenuNode.objects.create(parent=root, url='one', is_named_url=False, text='one')
        ch_1_1 = MenuNode.objects.create(parent=ch1, url='one_one', is_named_url=False, text='one_one')
        ch_1_2 = MenuNode.objects.create(parent=ch1, url='one_two', is_named_url=False, text='one_two')
        ch2 = MenuNode.objects.create(parent=root, url='two', is_named_url=False, text='two')
        ch2_1 = MenuNode.objects.create(parent=ch2, url='two_one', is_named_url=False, text='two_one')
        ch2_1_1 = MenuNode.objects.create(parent=ch2_1, url='two_one_one', is_named_url=False,
                                          text='two_one_one')
        result = listed_tree2dict(root.descendants(include_self=True))
        self.assertEqual({'text': 'root', 'url': 'root', 'is_selected': False, 'children': [
            {'text': 'one', 'url': 'one', 'is_selected': False,
             'children': [{'text': 'one_one', 'url': 'one_one', 'is_selected': False},
                          {'text': 'one_two', 'url': 'one_two', 'is_selected': False}]},
            {'text': 'two', 'url': 'two', 'is_selected': False, 'children': [
                {'text': 'two_one', 'url': 'two_one', 'is_selected': False,
                 'children': [{'text': 'two_one_one', 'url': 'two_one_one', 'is_selected': False}]}]}]}, result)
