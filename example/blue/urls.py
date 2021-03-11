from django.urls import path,include
from . import views


urlpatterns = [
    path('health/', views.test, name='health'),
    path('secret/', views.code, name='secret')
]
    