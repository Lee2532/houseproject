from attr import field
from rest_framework import serializers
from .models import Story, StoryComment

class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = [
            'title',
            'content'
        ]
        
class StoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        # field = '__all__'
        fields = [
            'story_idx',
            'author',
            'content',
        ]