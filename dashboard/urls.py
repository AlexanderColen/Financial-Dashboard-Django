"""
Define URL routes for entire project.
"""
from django.urls import include, path
from rest_framework import routers
from dashboard import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('expenditures.urls')),
    path('', include('income.urls')),
    path('', include('debt.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
