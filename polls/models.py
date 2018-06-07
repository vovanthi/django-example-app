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

class Categories(models.Model):
    class Meta:
        db_table = 'categories'
        unique_together = (('tag_id', 'category_id'),)
    tag_id = models.ForeignKey(
        'Tags',
        on_delete=models.DO_NOTHING,
        db_column='tag_id')
    # tag_id = models.IntegerField('タグID', primary_key=True)
    category_id = models.IntegerField('カテゴリID', primary_key=True)
    category_name = models.TextField('カテゴリ名', max_length=200)

