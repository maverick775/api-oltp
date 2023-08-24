from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from oltp.api import views
from .modules.customFunctions import trasnsfer

router = routers.DefaultRouter()
router.register(r'holders', views.HolderViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'movements', views.MovementViewSet)
router.register(r'accounts', views.AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/transfer/', trasnsfer)
]
urlpatterns += router.urls
