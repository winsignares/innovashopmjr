$(document).ready(function() {
    $(".estados").each(function() {
        var boton = $(this);
        var valor = boton.data("valor");
        if (valor !== undefined) {
            // Remover todas las clases de color
            boton.removeClass("activo inactivo pendiente");
            // Aplicar la clase correspondiente al estado
            switch (valor.toString().toLowerCase()) {
                case 'activo':
                    console.log("ACTIVO")
                    boton.addClass("activo");
                    break;
                case 'inactivo':
                    console.log("INACTIVO")
                    boton.addClass("inactivo");
                    break;
                case 'pendiente':
                    console.log("PENDIENTE")
                    boton.addClass("pendiente");
                    break;
            }
        }
    });
});
