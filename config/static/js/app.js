






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




function LoginUser() {
    let userIdInput = document.getElementById("idUser");
    let userPassInput = document.getElementById("passUser");
    let userId = userIdInput.value;
    let userPass = userPassInput.value;
    let endpoint = "validate_user";
    
    axios.post(endpoint, {
        'user': userId,
        'password': userPass
    })
    .then(function (response) {
        if (response.data.success) {
            toastr.success(response.data.message, "Success");
            userIdInput.style.border = "1px solid green";
            userIdInput.style.backgroundColor = "rgba(0, 255, 0, 0.1)"; // Fondo verde con opacidad
            userPassInput.style.border = "1px solid green";
            userPassInput.style.backgroundColor = "rgba(0, 255, 0, 0.1)"; // Fondo verde con opacidad
            setTimeout(function() {
                window.location.href = "/controller/Layout";
            }, 2000);
        } else {
            if (response.data.message === 'ErrorPass') {
                userIdInput.style.border = "1px solid green";
                userIdInput.style.backgroundColor = "rgba(0, 255, 0, 0.1)"; // Fondo verde con opacidad
                userPassInput.style.border = "1px solid red";
                userPassInput.style.backgroundColor = "rgba(255, 0, 0, 0.1)"; // Fondo rojo con opacidad
                
                // Borra el valor del campo de contraseña
                userPassInput.value = "";
                
                toastr.error('Contraseña Incorrecta', "Error");
            } else {
                userIdInput.value ='';
                userPassInput.value = "";
                userIdInput.style.border = "1px solid red";
                userIdInput.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
                userPassInput.style.border = "1px solid red";
                userPassInput.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
                toastr.error('Usuario no existe', "Error");
            }
        }
    })
    .catch(function (error) {
        console.error('Error validating user:', error);
    });
}

