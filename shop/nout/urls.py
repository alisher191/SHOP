from django.urls import path, include
from django.contrib import admin

from nout.views import NoutListVIiew, NoutCreateView, NoutDeteilView

app_name = 'Nout'
urlpatterns = [
    path('noutbuki/create/', NoutCreateView.as_view()),
    path('all/', NoutListVIiew.as_view()),
    path('nout/deteil/<int:pk>/', NoutDeteilView.as_view()),
    
]
