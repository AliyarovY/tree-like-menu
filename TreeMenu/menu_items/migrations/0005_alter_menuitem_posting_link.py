# Generated by Django 4.2 on 2023-04-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0004_alter_menuitem_posting_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='posting_link',
            field=models.CharField(default='/', max_length=255),
        ),
    ]
