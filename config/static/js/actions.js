document.addEventListener("DOMContentLoaded", function(event) {
    // Recuperar el estado seleccionado del módulo de sessionStorage
    var moduloSeleccionado = sessionStorage.getItem("moduloSeleccionado");
    if (moduloSeleccionado) {
        var modulos = document.querySelectorAll('.modulo-box');
        modulos.forEach(function(element) {
            if (element.dataset.target === moduloSeleccionado) {
                element.classList.add('seleccionado');
            }
        });
    }
});

window.addEventListener("beforeunload", function(event) {
    // Guardar el estado seleccionado del módulo en sessionStorage
    var seleccionado = document.querySelector('.seleccionado');
    if (seleccionado) {
        var target = seleccionado.dataset.target;
        sessionStorage.setItem("moduloSeleccionado", target);
    }
});

function selectModulo(modulo) {
    // Remover la clase 'seleccionado' de todos los módulos
    var modulos = document.querySelectorAll('.modulo-box');
    modulos.forEach(function(element) {
        element.classList.remove('seleccionado');
    });

    // Agregar la clase 'seleccionado' al módulo clickeado
    modulo.classList.add('seleccionado');

    // Agregar la clase 'deslizar' a todos los módulos, excepto al seleccionado
    modulos.forEach(function(element) {
        if (element !== modulo) {
            element.classList.add('deslizar');
        }
    });

    // Quitar la clase 'deslizar' después de un breve período de tiempo
    setTimeout(function() {
        modulos.forEach(function(element) {
            element.classList.remove('deslizar');
        });
    }, 300); // Ajusta este valor para que coincida con el tiempo de transición en CSS
}
