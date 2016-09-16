from rest_framework import serializers
from apps.projects.models import *
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(max_length=500, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'auth_token', 'email', 'first_name', 'last_name',
                  'gender', 'avatar', 'date_created',)


class IssueImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueImage
        fields = ('image', )


class IssueVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueVideo
        fields = ('video', )


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeDocument
        fields = ('id', 'title', 'description', 'document', 'date_created')


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeAudio
        fields = ('id', 'title', 'description', 'audio', 'date_created')


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArticle
        fields = ('id', 'title', 'description', 'image', 'date_created')


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryVideo
        fields = ('id', 'title', 'description', 'video', 'date_created')


class CommentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentCategory
        fields = ('id', 'name')


class IssueSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)
    images = IssueImageSerializer(source='get_images', many=True)
    videos = IssueVideoSerializer(source='get_videos', many=True)
    number_of_comments = serializers.CharField(source='num_of_comments')

    class Meta:
        model = Issue
        fields = ('id', 'author', 'project', 'title', 'description',
                  'images', 'videos', 'number_of_comments' )


class IssueCommentSerializer(serializers.ModelSerializer):

    rating = serializers.CharField(source='get_rating')
    elapsed_time = serializers.CharField(source='get_elapsed_time')
    author = UserSerializer(many=False)

    class Meta:
        model = IssueComment
        fields = ('id', 'comment', 'rating', 'author',
                  'elapsed_time', 'image', 'video', 'audio')
