from django.urls import path
from debt import views

urlpatterns = [
    path('debt/', views.DebtList.as_view()),
    path('debt/<int:pk>/', views.DebtDetail.as_view()),
    path('payments/', views.PaymentList.as_view()),
    path('payments/<int:pk>/', views.PaymentDetail.as_view()),
]
