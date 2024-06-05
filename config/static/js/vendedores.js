function CrearVendedor() {
    let identificacion = document.getElementById("identificacion_vendedor").value;
    let nombre = document.getElementById("nombre_vendedor").value;
    let telefono = document.getElementById("telefono_vendedor").value;
    let nameEmpresa = document.getElementById("empresa").innerText;
    
    if (identificacion && nombre && telefono) {
        let endpoint = "/controller/CrearVendedor";

        axios.post(endpoint, {
            'iden': identificacion,
            'nombre': nombre,
            'telefono': telefono,
            'empresa': nameEmpresa
        })
        .then(function (response) {
            Swal.fire({
                icon: 'success',
                title: 'Vendedor creado!',
                text: 'El vendedor se ha creado exitosamente',
                confirmButtonText: 'Aceptar'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.reload();
                }
            });
        })
        .catch(function (error) {
            console.error('Error creating vendedor:', error);
        });
    } else {
        Swal.fire(
            'Faltan campos',
            'Por favor completa todos los campos.',
            'error'
        );
    }
}




function EliminarVendedor(id) {
    let idDelete = id;
    let endpoint = "/controller/EliminarVendedor";
    
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
                    'El Vendedor ha sido eliminado.',
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

