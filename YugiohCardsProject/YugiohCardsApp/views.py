from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
  
    try:
            response = requests.get(base_url)
            response.raise_for_status()
            data = response.json()
            
            cards = []  # Lista para armazenar os dados dos cards

            if data["data"]:
                for resultados in data["data"]:
                    cards_info = {
                        "id": resultados["id"],
                        "image": resultados["card_images"][0]["image_url"],
                        "name": resultados["name"],
                        "type": resultados["type"],
                        "frameType": resultados["frameType"],
                        "desc": resultados["desc"],
                        # "atk": resultados["atk"],
                        # "def": resultados["def"],
                        # "level": resultados["level"],
                        "race": resultados["race"],
                        # "attribute": resultados["attribute"],
                    }
                    cards.append(cards_info)

                # Use slice para pegar apenas os primeiros 25 itens
                cards = cards[:125]

                contexto = {"cards": cards}
 
    except requests.exceptions.RequestException as e:
            print(f"Erro na solicitação HTTP: {e}")
            contexto = {"cards": []}  # Lista vazia em caso de erro

    return render(request, 'home.html', contexto)
