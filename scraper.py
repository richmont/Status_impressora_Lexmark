import requests
from bs4 import BeautifulSoup

ip = '10.127.244.21'
"""
# Coletar a primeira página da lista de artistas
page = requests.get('http://10.127.244.21/cgi-bin/dynamic/printer/PrinterStatus.html')
soup = BeautifulSoup(page.text, 'html.parser')

Status de suprimento de papel fica específicamente sob o estilo
padding: .75pt
0 = Bandeja 1
1 = Bandeja 2
2 = MF Alimentador
3 = Bandeja Padrão

"""
# finalmente consegui isolar o "ok"


def scraper_pagina(ip):
    """
    Recebe um endereço e retorna um objeto beautifulsoup
    """
    endereco = str('http://' + ip + '/cgi-bin/dynamic/printer/PrinterStatus.html')
    pagina = requests.get(endereco)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    return soup


def filtragem(soup):
    """
    recebe um objeto beautifulsoup
    retorna 4 variáveis com o status das bandejas em forma de texto
    """

    resultado = soup.findAll("table", {"style": "padding: .75pt"})
    bandeja_1 = resultado[0].find_all("b", text=True)[0].text
    bandeja_2 = resultado[1].find_all("b", text=True)[0].text
    mf_alimentador = resultado[2].find_all("b", text=True)[0].text
    bandeja_padrao = resultado[3].find_all("b", text=True)[0].text
    return bandeja_1, bandeja_2, mf_alimentador, bandeja_padrao


soup = scraper_pagina(ip)
bandeja_1, bandeja_2, mf_alimentador, bandeja_padrao = filtragem(soup)
"""
print("Bandeja 1: ", bandeja_1)
print("Bandeja 2: ", bandeja_2)
print("MF Alimentador: ", mf_alimentador)
print("Bandeja Padrão: ", bandeja_padrao)
"""
