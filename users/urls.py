from django.urls import path
from . import views

# para cargar Images
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    #user urls
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('index', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.logout_request, name='logout_request'),
    path('setting', views.setting, name='setting'),
    path('profile', views.profile, name='profile'),
    path('user-edit', views.editar_user, name='editar_user'),
    
    # web scraping con hoteles
    path('hospedaje', views.hospedaje, name='hospedaje'),
    path('hospedaje2', views.hospedaje2, name='hospedaje2'),
    path('experiancia-culinaria', views.expe_culinaria, name='expe_culinaria'),
    path('para-hacer', views.para_hacer, name='para_hacer'),
    path('para-hacer2', views.para_hacer2, name='para_hacer2'),
    path('restaurantes', views.restaurantes, name='restaurantes'),
    path('restaurantes2', views.restaurantes2, name='restaurantes2'),
    
    path('hoteles', views.hoteles, name='hoteles'),
    path('crear-hotel', views.crear_hotel, name='crear_hotel'),
    path('borrar-hotel/<int:id>', views.borrar_hotel, name='borrar_hotel'),
    path('editar-hotel/<int:id>', views.editar_hotel, name='editar_hotel'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



















