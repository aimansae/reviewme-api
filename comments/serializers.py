from .models import Comment
from rest_framework import serializers

# Credit CI walkthough


class CommentSerializer(serializers.ModelSerializer):
    '''
    Serializer for COmment model
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

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
            'comment_text',
        ]


# Credit CI walkthough
class CommentDetailSerializer(CommentSerializer):
    '''
    Serializer for detail view
    '''
    review = serializers.ReadOnlyField(source='review.id')
