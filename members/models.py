from django.db import models

# Create your models here.
class Members(models.Model):
    member_id = models.TextField('メンバーID', max_length=100)
    member_name = models.TextField('メンバー名称', max_length=200)
    joined_at = models.DateTimeField('入会日時', null=True)
    insert_at = models.DateTimeField('登録日時', auto_now_add=True)
    insert_user = models.IntegerField('登録ユーザ', null=True)
    update_at=  models.DateTimeField('更新日時', auto_now=True)
    update_user = models.IntegerField('更新ユーザ', null=True)
