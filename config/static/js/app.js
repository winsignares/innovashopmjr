






document.addEventListener("DOMContentLoaded", function () {
    const lblText = document.getElementById("lblText");

    lblText.addEventListener("input", function () {
        if (this.value.length > 26) {
            this.value = this.value.slice(0, 26); // Limitar la longitud a 26 caracteres
        }
    });
});



$(document).ready(function() {
    $(".modulos").each(function() {
        var boton = $(this);
        var valor = boton.data("valor");
        if (valor !== undefined && valor.toString().toLowerCase() === 'true') {
            boton.find("img").css("opacity", "1"); 
        } else {
            boton.find("img").css("opacity", "0.2");
            
        }

        boton.click(function() {
            var nuevoValor = !valor; 
            boton.data("valor", nuevoValor);
            var empresaId = boton.closest('tr').find('.empresa-id').text();
            $.ajax({
                url: "actualizar_empresa",
                method: "POST", 
                contentType: "application/json", 
                data: JSON.stringify({"ID": empresaId, "modulo": boton.attr("id"), "boolean": valor.toString()}), // Convertir nuevoValor a una cadena
                success: function(respuesta) {
                    console.log('Actualización exitosa:', respuesta);
                    location.reload();
                    
                },
        
            });
            
        });
    });
});


$(document).ready(function() {
    $(".crearEmpresa").each(function() {
        var boton = $(this);
        boton.click(function() {
    
            $.ajax({
                url: "crear_empresa",
                method: "POST", 
                contentType: "application/json", 
                success: function(respuesta) {
                    console.log('Actualización exitosa:', respuesta);
        
                    
                },
        
            });
            
        });
    });
});
