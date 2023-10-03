from django.urls import path
from . import views

urlpatterns = [
    path('diaspora/', views.DiasporaList, name='diaspora'),
    path('add-diaspora/', views.addDiaspora, name='add-diaspora'),
    path('county/', views.county, name='county'),
    path('add-county/', views.addCounty, name='add-county'),
    # path('diaspora/<int:pk>/', views.DiasporaDetail),
]
