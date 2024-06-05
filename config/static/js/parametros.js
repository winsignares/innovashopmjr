function EditarParametros() {
    const id = document.getElementById('idEditar').value;
    const producto = document.getElementById('productoEditar').value;
    const precio = parseFloat(document.getElementById('precioEditar').value);
    const ganancia = parseFloat(document.getElementById('gananciaEditar').value);
    const iva = parseFloat(document.getElementById('ivaEditar').value);

    // Calcula el precio final sumando la ganancia y el IVA al precio base
    const precioFinal = precio + (precio * ganancia / 100) + (precio * iva / 100);
    
    let endpoint = "/controller/EditarParametros";
    
    axios.post(endpoint, {
        'id':id,
        'producto': producto,
        'precio': precio,
        'ganancia': ganancia,
        'iva': iva,
        'PrecioFinal': precioFinal
    })
    .then(function (response) {
        console.log(response);
        console.log(producto);
        // Muestra un mensaje de éxito utilizando SweetAlert2
        Swal.fire({
            icon: 'success',
            title: '¡Parámetros actualizados!',
            text: 'Los parámetros se han actualizado exitosamente.',
            confirmButtonText: 'Aceptar'
        }).then(() => {
            // Recarga la página después de cerrar el mensaje
            window.location.reload();
        });
    })
    .catch(function (error) {
        console.error('Error al editar los parámetros:', error);
        // Muestra un mensaje de error utilizando SweetAlert2
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Ha ocurrido un error al editar los parámetros.',
            confirmButtonText: 'Aceptar'
        });
    });
}
