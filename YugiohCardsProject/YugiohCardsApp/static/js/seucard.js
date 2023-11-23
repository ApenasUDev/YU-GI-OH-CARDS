function addToDeck(card) {
    // Extrair dados da carta
    var cardId = card.getAttribute("data-id-data");
    var cardImage = card.getAttribute("data-image-data");
    var cardName = card.getAttribute("data-nome-data");

    // Adicionar à área de construção do deck
    var deckBuilder = document.querySelector("#deck");
    var cardDiv = document.createElement("div");
    cardDiv.innerHTML = "<img src='" + cardImage + "' alt='" + cardName + "' data-id-data='" + cardId + "' onclick='removeFromDeck(event);'>";
    deckBuilder.appendChild(cardDiv);
}

function removeFromDeck(event) {
    // Verificar se o clique foi em uma carta no deck
    if (event.target.tagName === 'IMG') {
        // Extrair o ID da carta
        var cardId = event.target.getAttribute("data-id-data");

        // Encontrar e remover a carta do deck
        var deckBuilder = document.querySelector("#deck");
        var cardToRemove = deckBuilder.querySelector("[data-id-data='" + cardId + "']");
        if (cardToRemove) {
            deckBuilder.removeChild(cardToRemove);
        }
    }
}