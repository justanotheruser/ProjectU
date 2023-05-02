from django.db import models
from .django_tree_queries.tree_queries.models import TreeNode


class MenuNode(TreeNode):
    url = models.CharField(max_length=500)
    is_named_url = models.BooleanField()
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Menu(models.Model):
    root_node = models.ForeignKey(MenuNode, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
