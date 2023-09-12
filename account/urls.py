from django.urls import path,include
from.views import*

urlpatterns = [
    path('reg',RegView.as_view(),name='h'),
    path("lgout",LgOutView.as_view(),name='lgout')
]

