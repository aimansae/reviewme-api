from rest_framework import serializers
from .models import Save
from django.db import IntegrityError


class SaveSerializer(serializers.ModelSerializer):
    '''
    Serializer for Save Model
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save
        fields = '__all__'

# to handle duplicates, credit CI walkthrough
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail: You Already saved this review'
            })
