function addToDeck(card) {
    // Extrair dados da carta
    var cardId = card.getAttribute("data-id-data");
    var cardImage = card.getAttribute("data-image-data");
    var cardName = card.getAttribute("data-nome-data");
    // ... extrair outros dados conforme necessário

    // Adicionar à área de construção do deck
    var deckBuilder = document.querySelector(".deck-builder");
    var cardDiv = document.createElement("div");
    cardDiv.innerHTML = "<img src='" + cardImage + "' alt='" + cardName + "'>";
    deckBuilder.appendChild(cardDiv);
}