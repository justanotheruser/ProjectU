# Generated by Django 4.2 on 2023-04-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menus', '0003_treemenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menunode',
            name='url',
            field=models.CharField(default='', max_length=500),
        ),
    ]