from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
import requests

# Create your views here.
# criando funçõs par filtrar os cards
def FilterCard(resultados):
 
                    if resultados["type"] == "Trap Card" or resultados["type"] == "Spell Card":
                        cards_info = {
                            "id": resultados["id"],
                            "image": resultados["card_images"][0]["image_url"],
                            "name": resultados["name"],
                            "type": resultados["type"],
                       
                            "desc": resultados["desc"],                     
                            "race": resultados["race"],
                           
                        }
                    else:
                        cards_info = {
                            "id": resultados["id"],
                            "image": resultados["card_images"][0]["image_url"],
                            "name": resultados["name"],
                            "type": resultados["type"],
                            "desc": resultados["desc"],
                            "atk": resultados.get("atk", None),  # Use get() para obter "atk" com um valor padrão se estiver ausente
                            "def": resultados.get("def", None),  # Use get() para obter "def" com um valor padrão se estiver ausente
                            "level": resultados.get("level", None),  # Use get() para obter "level" com um valor padrão se estiver ausente
                            "race": resultados["race"],
                            "attribute": resultados.get("attribute",None),
                        }
                    return cards_info
def home(request):
    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
  
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        
        cards = []  # Lista para armazenar os dados dos cards

        if data["data"]:
            for resultados in data["data"]:
                cards_info = FilterCard(resultados)
                cards.append(cards_info)

            # # Use slice para pegar apenas os primeiros 125 itens
            # cards = cards[:125]

            # Configuração da paginação
            paginator = Paginator(cards, 150)  # 10 itens por página
            page_number = request.GET.get('page', 1)

            try:
                cards = paginator.page(page_number)
            except EmptyPage:
                cards = paginator.page(paginator.num_pages)

            contexto = {"cards": cards}
            print(len(cards))
 
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
        contexto = {"cards": []}  # Lista vazia em caso de erro

    return render(request, 'home.html', contexto)

def buscar_card(request):
    nome_card = request.GET.get('nome_card', '') 
    try:
                       # Acesse o valor do botão de rádio selecionado usando request.GET
            tipo_selecionado = request.GET.get("tipo")
                        
                        # Agora, você pode usar o valor para tomar a ação necessária
            if tipo_selecionado == "opcao1":
                        BASE_URL = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?type={nome_card}"
            elif tipo_selecionado == "opcao2":
                        BASE_URL = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?attribute={nome_card}"
            elif tipo_selecionado == "opcao3":      
                        BASE_URL = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?race={nome_card}"
            else:
                        BASE_URL = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={nome_card}"
            response = requests.get(BASE_URL)
            response.raise_for_status()
            data = response.json()
            
            cards = []  # Lista para armazenar os dados dos cards

            if data["data"]:
                for resultados in data["data"]:
                            
                    cards_info = FilterCard(resultados)

                    cards.append(cards_info)

                contexto = {"cards": cards}
              
 
    except requests.exceptions.RequestException as e:
            print(f"Erro na solicitação HTTP: {e}")
            contexto = {"cards": []}  # Lista vazia em caso de erro

    return render(request, 'home.html', contexto)

def deck(request):
    return render(request,'deck.html')