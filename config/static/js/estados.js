document.addEventListener("DOMContentLoaded", function () {
    // Obtener todas las celdas de stock en la tabla
    const stockCells = document.querySelectorAll("#stock-body td:nth-child(4)"); // El cuarto 'td' en cada fila es donde se muestra el stock

    // Iterar sobre cada celda de stock y establecer la imagen correspondiente
    stockCells.forEach(function(cell) {
        const stock = parseInt(cell.textContent); // Obtener el valor de stock como entero
        const stockImageSpan = document.createElement("span");

        // Función para establecer la imagen según el valor de stock
        function setStockImage(stock) {
            let imagePath = '';
            let altText = '';
            let imageSize = '';

            if (stock === 0) {
                imagePath = './static/img/rojo.png';
                altText = 'Stock 0';
                imageSize = 'small';
            } else if (stock >= 1 && stock <= 100) {
                imagePath = './static/img/naranja.png';
                altText = 'Stock 1-10';
                imageSize = 'small';
            } else {
                imagePath = './static/img/verde.png';
                altText = 'Stock 10+';
                imageSize = 'small';
            }

            stockImageSpan.innerHTML = `<img src="${imagePath}" alt="${altText}" class="${imageSize}">`;
        }

        // Llamar a la función para establecer la imagen del stock
        setStockImage(stock);

        // Insertar el elemento de imagen dentro del 'span' en la celda de stock
        cell.innerHTML = ''; // Limpiar el contenido actual de la celda
        cell.appendChild(stockImageSpan);
    });
});
