from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login_view'),
    path('index', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('hospedaje', views.hospedaje, name='hospedaje'),
    path('experiancia-culinaria', views.expe_culinaria, name='expe_culinaria'),
    path('tabla', views.tabla, name='tabla')
]



















