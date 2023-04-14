from django.db import models

NULLABLE = dict(blank=True, null=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField()
    posting_link = models.CharField(default='/', max_length=255)
    parent = models.ForeignKey(
        to='self',
        **NULLABLE,
        default=None,
        on_delete=models.SET_NULL,
        related_name='childs',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu_item'
        verbose_name = 'MenuItem'
        verbose_name_plural = 'MenuItems'
