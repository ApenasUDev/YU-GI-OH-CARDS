
    document.addEventListener("DOMContentLoaded", function () {
        const images = document.querySelectorAll(".card-image");
        const modal = document.getElementById("modal");
        const modalContent = document.getElementById("modal-content");
        const close = document.querySelector(".close");

        images.forEach((image) => {
            image.addEventListener("click", () => {
                modal.style.display = "block";

                // Obtenha os dados associados à imagem clicada (substitua por seus próprios dados)
                const idData = image.getAttribute("data-id-data");
                const imageData = image.getAttribute("data-image-data");
                const nameData = image.getAttribute("data-nome-data");
                const typeData = image.getAttribute("data-type-data");
                const decData = image.getAttribute("data-desc-data");
                const raceData = image.getAttribute("data-race-data");
                const atkData = image.getAttribute("data-atk-data");
                const defData = image.getAttribute("data-def-data");
                const levelData = image.getAttribute("data-level-data");
                const attributeData = image.getAttribute("data-attribute-data");

                // Atualize o conteúdo do modal com os dados da imagem
                if (typeData == "Trap Card" || typeData == "Spell Card") {
                    modalContent.innerHTML = `<div>
                        <h2>Detalhes do Card</h2>
                        <div class="flex-container">
                            <div>
                                <img src="${imageData}" alt="Card Image" style="max-width: 450px; ">
                            </div>
                                <div>
                                <h2>id: ${idData} | nome: ${nameData}</h2>
                                <h2>tipo: ${typeData}</h2>
                                <h2>raça: ${raceData}</h2>
                                <h2 style="background-color:green;color:white;width:20%;">descrição: </h2><p>${decData}</p>

                            </div>
                    `;
                } else {
                    modalContent.innerHTML = `<d

Python 97.6%
Other 2.4%iv>
                        <h2>Detalhes do Card</h2>
                        <div class="flex-container">
                            <div>
                                <img src="${imageData}" alt="Card Image" style="max-width: 450px; ">
                            </div>
                                <div>
                                <h2>id: ${idData} | nome: ${nameData}</h2>
                                <h2>tipo: ${typeData}</h2>
                                <h2>raça: ${raceData}</h2>
                                <h2>atk: ${atkData} | def: ${defData}</h2>
                                <h2>level: ${levelData}</h2>
                                <h2>atributo: ${attributeData}</h2>
                                <h2 style="background-color:green;color:white;width:20%;">descrição: </h2><p>${decData}</p>
                            </div>
                               
                        </div>
                    </div>
                    `;
                }

            });
        });

        close.addEventListener("click", () => {
            modal.style.display = "none";
        });

        window.addEventListener("click", (event) => {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        });
    });
