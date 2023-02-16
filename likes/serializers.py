from rest_framework import serializers
from .models import Like
from django.db import IntegrityError


class LikeSerializer(serializers.ModelSerializer):
    '''
    Serializer foe like model
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'created_at',
            'owner',
            'review',
        ]

# to handle duplicates, credit CI walkthrough
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                detail: 'You Already liked this review'
            })
