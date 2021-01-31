"""
Define URL routes for Income component.
"""
from django.urls import path
from income import views

urlpatterns = [
    path('income/', views.IncomeList.as_view()),
    path('income/<int:pk>/', views.IncomeDetail.as_view()),
    path('types/', views.IncomeTypeList.as_view()),
    path('types/<int:pk>/', views.IncomeTypeDetail.as_view()),
]
