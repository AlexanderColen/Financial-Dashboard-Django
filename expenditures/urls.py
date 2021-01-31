from django.urls import path
from expenditures import views

urlpatterns = [
    path('expenditures/', views.ExpenditureList.as_view()),
    path('expenditures/<int:pk>/', views.ExpenditureDetail.as_view()),
    path('types/', views.TypeList.as_view()),
    path('types/<int:pk>/', views.TypeDetail.as_view()),
]
