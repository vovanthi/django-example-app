from rest_framework import serializers
from .models import Members

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = (
            'member_id',
            'member_name',
            'joined_at'
            )