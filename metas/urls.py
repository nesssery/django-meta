from django.urls import path
from metas import views

urlpatterns = [
    path('', views.index, name="index"),
    path('opengraph/', views.opengraph, name="opengraph"),
    path('sekizai/', views.sekizai, name="sekizai"),
]
