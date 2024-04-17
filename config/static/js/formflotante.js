// Función para mostrar u ocultar el modal
function toggleModal() {
    var modal = document.getElementById("modal");
    modal.style.display = (modal.style.display === "block") ? "none" : "block";
}

// Función para crear una empresa (simulada)
function crearEmpresa() {
    // Obtener los valores de los campos del formulario
    var nombre_empresa = document.getElementById("nombre_empresa").value;
    var periodo_actividad = document.getElementById("periodo_actividad").value;
    
    // Obtener el estado de cada aspecto del módulo
    var aspecto1 = document.getElementById("aspecto1").checked;
    var aspecto2 = document.getElementById("aspecto2").checked;
    // Repite para los demás aspectos del módulo

    // Aquí puedes enviar los datos a través de AJAX o hacer lo que necesites con ellos
    console.log("Nombre de la empresa:", nombre_empresa);
    console.log("Período de actividad:", periodo_actividad);
    console.log("Aspecto 1:", aspecto1);
    console.log("Aspecto 2:", aspecto2);
}
