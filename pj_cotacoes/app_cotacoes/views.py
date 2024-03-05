from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    # Passando a url para uma variável(também pode ser requisitada diretamente)
    usd_url = f'http://economia.awesomeapi.com.br/json/last/USD-BRL'
    eur_url = f'http://economia.awesomeapi.com.br/json/last/EUR-BRL'
    
    # Requisitando as informações da API
    usd_response = requests.get(usd_url)
    eur_response = requests.get(eur_url)
    
    # Armazenando as informalções obtidas em json em uma variável
    usd_data = usd_response.json()
    eur_data = eur_response.json()
    
    # Extraindo apenas as informações que me interessam do 'dicionário'
    usd_to_brl = usd_data['USDBRL']['ask']
    eur_to_brl = eur_data['EURBRL']['ask']
    
    # Processando as informações
    return render(request, 'app_cotacoes/home.html', {'usd_to_brl': usd_to_brl, 'eur_to_brl': eur_to_brl}) 