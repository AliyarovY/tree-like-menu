# Generated by Django 4.2 on 2023-04-14 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MunuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(unique=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childs', to='menu_items.munuitem')),
            ],
            options={
                'verbose_name': 'MenuItem',
                'verbose_name_plural': 'MenuItems',
                'db_table': 'menu_items',
            },
        ),
    ]
