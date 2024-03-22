document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const columnSelector = document.getElementById("column-selector");
    const tableBody = document.getElementById("stock-body");
    const rowsPerPage = 5;

    // Función para filtrar los datos en la tabla
    function filterTable() {
        const searchText = searchInput.value.toLowerCase();
        const columnIndex = columnSelector.selectedIndex;
        const rows = tableBody.querySelectorAll("tr");

        let visibleRowCount = 0;

        rows.forEach(row => {
            const cells = row.querySelectorAll("td");
            const targetCell = cells[columnIndex];
            const cellText = targetCell.textContent.toLowerCase();

            if (cellText.includes(searchText)) {
                row.style.display = "";
                visibleRowCount++;
            } else {
                row.style.display = "none";
            }
        });

        // Si el campo de búsqueda está vacío, limitar la tabla a 10 datos
        if (searchText === "") {
            rows.forEach((row, index) => {
                if (index < rowsPerPage) {
                    row.style.display = "";
                    visibleRowCount++;
                } else {
                    row.style.display = "none";
                }
            });
        }

        // Limitar los resultados de búsqueda a 10 datos
        if (searchText !== "" && visibleRowCount > rowsPerPage) {
            rows.forEach((row, index) => {
                if (index >= rowsPerPage) {
                    row.style.display = "none";
                }
            });
        }

        // Mostrar u ocultar botones de página anterior y siguiente
        const nextPageBtn = document.getElementById("next-page");
        nextPageBtn.disabled = visibleRowCount <= rowsPerPage;
    }

    // Evento al escribir en el campo de búsqueda
    searchInput.addEventListener("input", filterTable);

    // Función para llenar automáticamente el selector de columna
    function populateColumnSelector() {
        const headers = document.querySelectorAll("#stock-table th");
        headers.forEach((header, index) => {
            const option = document.createElement("option");
            option.text = header.textContent.trim();
            option.value = index;
            columnSelector.appendChild(option);
        });
    }

    // Llenar el selector de columna al cargar la página
    populateColumnSelector();
});
