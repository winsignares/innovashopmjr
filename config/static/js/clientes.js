function CrearCliente() {
    let identificacion = document.getElementById("identificacion_cliente").value;
    let nombre = document.getElementById("nombre_cliente").value;
    let telefono = document.getElementById("telefono_cliente").value;
    let nameEmpresa = document.getElementById("empresa").innerText;

    console.log(identificacion,nombre,telefono,nameEmpresa);
    
    if (identificacion && nombre && telefono) {
        let endpoint = "/controller/CrearCliente";

        axios.post(endpoint, {
            'iden': identificacion,
            'nombre': nombre,
            'telefono': telefono,
            'empresa': nameEmpresa
        })
        .then(function (response) {
            Swal.fire({
                icon: 'success',
                title: 'Cliente creado!',
                text: 'El cliente se ha creado exitosamente',
                confirmButtonText: 'Aceptar'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.reload();
                }
            });
        })
        .catch(function (error) {
            console.error('Error creating cliente:', error);
        });
    } else {
        Swal.fire(
            'Faltan campos',
            'Por favor completa todos los campos.',
            'error'
        );
    }
}



function EliminarCliente(id) {
    let idDelete = id;
    let endpoint = "/controller/EliminarCliente";
    
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminarlo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            axios.post(endpoint, {
                'id': idDelete,
            })
            .then(function (response) {
                Swal.fire(
                    'Eliminado!',
                    'El Cliente ha sido eliminado.',
                    'success'
                );
                window.location.reload(); // Recargar la página después de eliminar el producto
            })
            .catch(function (error) {
                console.error('Error al eliminar el producto:', error);
            });
        }
    });
}
