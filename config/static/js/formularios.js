function mostrarFormulario() {
    var formulario = document.getElementById("crear-form-container");
    formulario.classList.add("active");
}

function cerrarFormulario() {
    var formulario = document.getElementById("crear-form-container");
    formulario.classList.remove("active");
}