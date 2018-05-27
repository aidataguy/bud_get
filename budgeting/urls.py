from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.project_list.as_view()),
    # path('project', views.project_list.as_view()),
    path('<int:pk>', views.project_detail.as_view()),
    path('category', views.category_list.as_view()),
    path('category/<int:pk>', views.category_detail.as_view()),
    path('expense/', views.expense_list.as_view()),
    path('expense/<int:pk>', views.expense_detail.as_view()),
]
