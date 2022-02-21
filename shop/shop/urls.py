
from django.contrib import admin
from django.urls import path, include
from nout.views import NoutViewSet
from .yasg import urlpatterns_yasg




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/nout/', include('nout.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls')),


]

urlpatterns += urlpatterns_yasg
