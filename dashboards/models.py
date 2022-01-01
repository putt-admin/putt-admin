from enum import Enum

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class ModelBase(models.Model):
    is_active = models.BooleanField(_('is_active'), default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True, auto_now=True)


class Projects(ModelBase):
    name = models.CharField(_('name'), max_length=31, db_index=True)
    remark = models.CharField(_('remark'), max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'projects'
        verbose_name = _('Projects')
        verbose_name_plural = _('Projects')


class Menus(ModelBase):
    name = models.CharField(_('name'), max_length=31, db_index=True)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)

    class Meta:
        db_table = "menus"
        verbose_name = _('Menus')
        verbose_name_plural = _("Menus")
        unique_together = ('name', 'project',)


class MetaTable(ModelBase):
    table_name = models.CharField(_('Table Name'), max_length=31)
    menu = models.ForeignKey(to=Menus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'meta_tables'
        verbose_name = _('Meta-tables')
        verbose_name_plural = _('Meta-tables')


class MetaField(ModelBase):
    class TYPE_CHOICES(Enum):
        CharField = 'CharField'
        IntegerField = 'IntegerField'
        DateTimeField = 'DateTimeField'
        BooleanField = 'BooleanField'

    field_name = models.CharField(_('Field Name'), max_length=31)
    table = models.ForeignKey(to=MetaTable, on_delete=models.CASCADE)
    field_type = models.CharField(_('Type'), max_length=31, choices=[(i.name, i.value,) for i in TYPE_CHOICES])
    max_length = models.IntegerField(_('max_length'))
    default_value = models.CharField(_('default_value'), max_length=255)

    class Meta:
        db_table = 'meta_fields'
        verbose_name = _('Meta-Fields')
        verbose_name_plural = _('Meta-Fields')
