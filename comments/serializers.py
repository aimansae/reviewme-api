from .models import Comment
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


# Credit CI walkthough
class CommentSerializer(serializers.ModelSerializer):
    '''
    Serializer for Comment Model
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'review',
            'created_at',
            'updated_at',
            'content',
        ]


# Credit CI walkthough
class CommentDetailSerializer(CommentSerializer):
    '''
    Serializer for detail view
    '''
    review = serializers.ReadOnlyField(source='review.id')
