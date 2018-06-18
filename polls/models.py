import datetime

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Tags(models.Model):
    class Meta:
        db_table = 'tags'
    tag_id = models.IntegerField('タグID', primary_key=True)
    tag_name = models.TextField('タグ名', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Categories(models.Model):
    class Meta:
        db_table = 'categories'
    tag_id = models.ForeignKey(
        'Tags',
        on_delete=models.DO_NOTHING,
        db_column='tag_id')
    category_name = models.TextField('カテゴリ名', max_length=200)

