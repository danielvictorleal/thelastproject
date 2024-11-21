from django.urls import path
from . import views

urlpatterns = [
    path('', views.ColecaoListCreate.as_view(), name='colecao-list-create'),
    path('<int:pk>/', views.ColecaoDetail.as_view(), name='colecao-detail'),
]