






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
    
    let endpoint = "/controller/validarUser";
    
    axios.post(endpoint, {
        'user': userId,
        'password': userPass
    })
    .then(function (response) {
        let role = response.data.rol;
        
        if (role === "ADMIN" || role === "EMPRESA" || role === "VENDEDOR") {
            Swal.fire({
                icon: 'success',
                title: '¡Inicio de sesión exitoso!',
                text: response.data.message,
                timer: 2000,
                timerProgressBar: true,
                showConfirmButton: false
            }).then(() => {
                window.location.href = "/panel";
            });
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: response.data.message
            }).then((result) => {
                if (result.isConfirmed) {
                    // Si el usuario no existe, resetear la página
                    location.reload();
                }
            });
            console.error('Rol desconocido:', role);
        }
    })
    .catch(function (error) {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Ha ocurrido un error al validar el usuario.'
        }).then((result) => {
            if (result.isConfirmed) {
                // Si hay un error, borrar el dato de la contraseña
                userPassInput.value = "";
                userPassInput.focus();
            }
        });
        console.error('Error validating user:', error);
    });
}

