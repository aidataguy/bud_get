from rest_framework import generics
from . import serializers
from . import models



class project_list(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class project_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class category_list(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class category_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class expense_list(generics.ListCreateAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


class expense_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


