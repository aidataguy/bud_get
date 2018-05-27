from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'budget',
        )
        model = models.Project

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'project',
            'name',
        )
        model = models.Category

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'project',
            'title',
            'amount',
            'category',
            'name',
            'budget'
        )
        model = models.Expense