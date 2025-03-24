
from django.urls import path
from sistema import views
#informa qual será a rota que ele irá chamaar determinada view(função).
urlpatterns = [
    path('sistema/', views.index),
]