from django.urls import path
from . import views

urlpatterns = [
    path('diaspora/', views.DiasporaList, name='diaspora'),
    path('add-diaspora/', views.addDiaspora, name='add-diaspora'),
    # path('diaspora/<int:pk>/', views.DiasporaDetail),
]
