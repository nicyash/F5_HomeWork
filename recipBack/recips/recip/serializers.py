from rest_framework import serializers
from .models import Category, Recips


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category')


class RecipsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recips
        fields = ('id', 'category', 'title', 'text')
