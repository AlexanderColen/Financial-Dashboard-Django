"""
Define URL routes for Expenditures component.
"""
from django.urls import path
from expenditures import views

urlpatterns = [
    path('expenditures/', views.ExpenditureList.as_view()),
    path('expenditures/<int:pk>/', views.ExpenditureDetail.as_view()),
    path('expendituretypes/', views.ExpenditureTypeList.as_view()),
    path('expendituretypes/<int:pk>/', views.ExpenditureTypeDetail.as_view()),
]
