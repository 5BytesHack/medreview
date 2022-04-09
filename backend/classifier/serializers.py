from rest_framework import serializers
from .models import Review
from .classifier_model import classify


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ['user', 'fio', 'mail', 'text']

    def create(self, validated_data):
        reviewed = classify(validated_data['text'])
        return Review.objects.create(
            author=self.user,
            fio=validated_data['fio'],
            mail=validated_data['mail'],
            text=validated_data['text'],
            reviewed=reviewed
        )

    def update(self, instance, validated_data):

        instance.pop('reviewed')

        for key, value in instance.items():
            setattr(instance, key, value)

        if validated_data:
            setattr(instance, 'reviewed', True)
        else:
            setattr(instance, 'reviewed', False)

        instance.save()

