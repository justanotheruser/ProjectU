# Generated by Django 4.2 on 2023-04-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menus', '0006_alter_menunode_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treemenu',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
