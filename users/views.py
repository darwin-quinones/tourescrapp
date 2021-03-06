from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from selenium import webdriver
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# importaciones de los modelos
from .models import Hotel, Profile
from django.contrib.auth.models import User
from django.contrib import messages
# forms 
from users.forms import ProfileForm, UserProfileForm
#ingreso user
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json

# django form
from users.forms import HotelForm

def home(request):
    return render(request, 'index/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # inicio de session
        user = authenticate(request, username=username, password=password)
        if user:
            
            login(request, user)
            messages.success(request, f'{user.username.capitalize()} logueado exitosamente')
            return redirect('index')
        else:
            messages.error(request, 'Username y contraseña incorrecta')
            return redirect('home')
    return redirect('home')

@login_required
def index(request):
    return render(request, 'index/index.html')

def sign_up(request):
    if(request.method == 'POST'):
        #se recibe la data que viene de la visata
        data = json.loads(request.body)
        
        #se crean nuevas variables
       
        genero = data['genero'].strip()
        tipo_identificacion = data['tipo_identificacion'].strip()
        identificacion = data['identificacion'].strip()
        fecha_naci = data['fecha_naci'].strip()
        telefono = data['telefono'].strip()
        lugar_reci = data['lugar_reci'].strip()
        username = data['username'].strip()
        password = data['password'].strip()

       
        #crear un nuevo user
        new_user = User.objects.create_user(username=username, password=password)
        new_user.first_name = data['nombres'].strip()
        new_user.last_name = data['apellidos'].strip()
        new_user.email = data['email'].strip()
        new_user.save()
        
        # crear un profile: se crea con una nueva instancia de la clase Profile
        profile = Profile(
            user=new_user, 
            telefono=telefono,
            genero=genero, 
            tipo_identificacion=tipo_identificacion, 
            identificacion=identificacion, 
            fecha_nacimiento=fecha_naci, 
            lugar_recidencia=lugar_reci
        )
        profile.save()
        return JsonResponse({'status': True})
    return redirect('home')

@login_required
def logout_request(request):
   
    logout(request)
    messages.success(request, 'Saliste Exitosamente')
    return redirect('home')

@login_required
def setting(request):
    return render(request, 'profile/setting.html')

@login_required
def profile(request):
    # se obtienen los datos del user
    user_id = request.user.id 
    user = Profile.objects.get(user_id=user_id)
 
    if request.method == 'POST':
        # se edita la img con el perfil
        form_img = ProfileForm(request.POST or None, request.FILES or None, instance=user)
       
        if form_img.is_valid():
            form_img.save()
        else:
            return redirect('profile')
            
   
    return render(request, 'profile/profile.html', {'user': user})


@login_required
def editar_user(request):
    user_id = request.user.id 
    user = Profile.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        
        form_user = UserProfileForm(request.POST or None, request.FILES or None, instance=request.user)
        content = {
            'form_user': form_user,
            'user': user
        }
        print(form_user)
        if form_user.is_valid():
            form_user.save()  
        else:
            print(form_user.errors)
            return render(request, 'profile/profile.html', content)
        
        return render(request, 'profile/profile.html', content)
    
    return redirect('profile')


@login_required
def hospedaje(request):
    
    hotels = Hotel.objects.all()
    return render(request, 'paginas/hospedaje/cards.html', {'hotels': hotels})


#hospedaje web scraping para mostrar hoteles
@login_required
def hospedaje2(request):
    
     # validacion de usuario
    if request.user.is_superuser:
        try:
            hotels = Hotel.objects.all()
        
        except Exception:
            pass
        return render(request, 'paginas/hospedajeAdmin/hospedajeAdmin.html', {'hotels': hotels})
    else:
        return redirect('index')
    
   

def expe_culinaria(request):
    return render(request, 'paginas/hospedaje/expe_culinaria.html')


@login_required
def restaurantes(request):
    return render(request, 'paginas/restaurante/restaurantes.html')

@login_required
def restaurantes2(request):
    return render(request, 'paginas/restauranteAdmin/restauranteAdmin.html')

@login_required
def para_hacer(request):
    return render(request, 'paginas/actividades/para_hacer.html')

@login_required
def para_hacer2(request):
    return render(request, 'paginas/actividadesAdmin/actividadesAdmin.html')

@login_required
def hoteles(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--log-level=3")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
    driver.get('https://www.tripadvisor.co/Hotels-g297473-oa30-Barranquilla_Atlantico_Department-Hotels.html')
    page = driver.page_source
    soup = BeautifulSoup(str(page), 'html.parser')
    hotelNames = soup.find_all('div', {'class': 'listing_title'})
    prices = soup.find_all('div', {'class': 'price-wrap'})
    i = 0
    for name in hotelNames:
        lists = "-- " * 2
        lists = lists.split()
        
        lists[0] = name.text.strip()
        lists[1] = prices[i].text
        # guardar hotesl en la base de datos
        Hotel.objects.create(nombre=name.text.strip(), precio=prices[i].text, status=1, imagen='imagenes/humildad.jpg', puntaje=5)
    
    print('Se hico el web scraping :)')
    return render(request, 'paginas/hospedaje/hoteles.html')

@login_required
def crear_hotel(request):
    # utilizacion de form
    formulario = HotelForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('hospedaje')
        
    return render(request, 'paginas/hospedajeAdmin/crear_hotel.html', {'formulario': formulario})

@login_required
def editar_hotel(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
    except Hotel.DoesNotExist as e:
        return redirect('hospedaje')
    # se ontienen los datos segun el id
    formulario = HotelForm(request.POST or None, request.FILES or None, instance=hotel)
    #actualizar cambios
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('hospedaje')
    return render(request, 'paginas/hospedajeAdmin/editar_hotel.html', {'formulario': formulario})

@login_required
def borrar_hotel(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
    except Hotel.DoesNotExist as e:
        return redirect('hospedaje')
    hotel.delete()
    return redirect('hospedaje')


