from rest_framework import serializers
from .models import Review, Answer
from .classifier_model import classify
from customauth.serializers import CustomUserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()

    class Meta:
        model = Review
        fields = ['author', 'fio', 'mail', 'text']

    def create(self, validated_data):
        title = classify(validated_data['text'])
        return Review.objects.create(
            author=validated_data['author'],
            fio=validated_data['fio'],
            mail=validated_data['mail'],
            text=validated_data['text'],
            title=title
        )

    def update(self, instance, validated_data):
        pass


class AnswerSerializer(serializers.ModelSerializer):

    review = ReviewSerializer(
        read_only=True
    )

    class Meta:
        model = Answer
        fields = ['text', 'review']

    def create(self, validated_data):
        return Answer.objects.create(

        )
