from rest_framework import serializers
from requests import post
from .models import Review, Answer
from customauth.serializers import CustomUserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Review
        fields = ['author', 'fio', 'mail', 'text']

    def create(self, validated_data):
        title = post('web:8080/', data={'text': validated_data['text']})
        return Review.objects.create(
            author=validated_data['author'],
            fio=validated_data['fio'],
            mail=validated_data['mail'],
            text=validated_data['text'],
            title=title
        )


class AnswerSerializer(serializers.ModelSerializer):

    review = ReviewSerializer(
        read_only=True
    )

    class Meta:
        model = Answer
        fields = ['text', 'review', 'author']

    def create(self, validated_data):
        return Answer.objects.create(
            text=validated_data['text'],
            review=validated_data['review'],
            author=validated_data['author']
        )
