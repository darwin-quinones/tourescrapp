from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import csv
from .models import User
from django.contrib import messages
from django.http import JsonResponse
import json



# Create your views here.
def home(request):
    return render(request, 'login.html')

def login(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        #print(email, password)
        try:
            user = User.objects.get(email=email)
            print(user.nombres)
            if user.password == password:
                request.session['id'] = user.id
                request.session['nombres'] = user.nombres
                request.session['email'] = user.email
                messages.success(request, f'{user.nombres.capitalize()} logueado exitosamente')
                return redirect('index')
            else:
                messages.error(request, 'Contraseña incorrecta')
                return redirect('home')

        except:
            messages.info(request, 'Correo incorrecto')
    return redirect('home')

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    if(request.method == 'POST'):
        #se recibe la data que viene de la visata
        data = json.loads(request.body)
        
        #se crean nuevas variables
        nombres = data['nombres'].strip()
        apellidos = data['apellidos'].strip()
        email = data['email'].strip()
        genero = data['genero'].strip()
        tipo_identificacion = data['tipo_identificacion'].strip()
        identificacion = data['identificacion'].strip()
        fecha_naci = data['fecha_naci'].strip()
        telefono = data['telefono'].strip()
        lugar_reci = data['lugar_reci'].strip()
        username = data['username'].strip()
        password = data['password'].strip()
        print(nombres, apellidos, email, genero, tipo_identificacion, identificacion, fecha_naci, telefono, lugar_reci, username, password)
        
        try:
            #se crea un nuevo user
            new_user = User.objects.create(
            nombres=nombres, apellidos=apellidos, email=email, username=username, password=password, telefono=telefono,
            genero=genero, tipo_identificacion=tipo_identificacion, identificacion=identificacion, fecha_nacimiento=fecha_naci, lugar_recidencia=lugar_reci)
        except:
           pass
        print(new_user)
        return JsonResponse({'status': True})
    return redirect('home')





def tabla(request):
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
        print(name.text.strip())
        lists[0] = name.text.strip()
        lists[1] = prices[i].text
        sheet = pd.read_csv('file.csv')
        df = pd.DataFrame([lists])
        df.to_csv("file.csv", index=False, mode='a', header=False)
        i = i + 1
    return render(request, 'tabla.html')
