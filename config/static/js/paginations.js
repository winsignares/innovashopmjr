document.addEventListener("DOMContentLoaded", function () {
    const tableBody = document.getElementById("stock-body");
    const prevPageBtn = document.getElementById("prev-page");
    const nextPageBtn = document.getElementById("next-page");
    const rowsPerPage = 10; // Cambiado a 5 datos por página
    let currentPage = 1;

    // Función para mostrar los datos correspondientes a la página actual
    function showCurrentPage() {
        const rows = tableBody.querySelectorAll("tr");
        const startIndex = (currentPage - 1) * rowsPerPage;
        const endIndex = Math.min(startIndex + rowsPerPage, rows.length); // Asegúrate de no pasar del último índice de fila
    
        rows.forEach((row, index) => {
            if (index >= startIndex && index < endIndex) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    
        // Mostrar u ocultar botones de página anterior y siguiente
        if (rows.length > rowsPerPage) {
            prevPageBtn.style.display = currentPage === 1 ? "none" : "";
            nextPageBtn.style.display = endIndex >= rows.length ? "none" : "";
        } else {
            prevPageBtn.style.display = "none";
            nextPageBtn.style.display = "none";
        }
    }
    

    // Mostrar la primera página al cargar
    showCurrentPage();

    // Evento al hacer clic en el botón de página anterior
    prevPageBtn.addEventListener("click", function () {
        if (currentPage > 1) {
            currentPage--;
            showCurrentPage();
        }
    });

    // Evento al hacer clic en el botón de página siguiente
    nextPageBtn.addEventListener("click", function () {
        const rows = tableBody.querySelectorAll("tr");
        const totalRows = rows.length;

        if (totalRows > currentPage * rowsPerPage) {
            currentPage++;
            showCurrentPage();
        }
    });
});