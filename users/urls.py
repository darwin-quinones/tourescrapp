from django.urls import path
from . import views

urlpatterns = [
    #user urls
    path('', views.home, name='home'),
    path('login', views.login_view, name='login_view'),
    path('index', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.logout_request, name='logout_request'),
    path('setting', views.setting, name='setting'),
    path('profile', views.profile, name='profile'),
    
    # web scraping con hoteles
    path('hospedaje', views.hospedaje, name='hospedaje'),
    path('experiancia-culinaria', views.expe_culinaria, name='expe_culinaria'),
    path('hoteles', views.hoteles, name='hoteles'),
    path('crear-hotel', views.crear_hotel, name='crear_hotel'),
    path('borrar-hotel/<int:id>', views.borrar_hotel, name='borrar_hotel'),
    path('editar-hotel/<int:id>', views.editar_hotel, name='editar_hotel'),
    
]



















