function CrearProducto() {
    let nombre = document.getElementById("nombre_producto");
    let stock = document.getElementById("stock_producto");
    let precio = document.getElementById("precio_producto");
    let categoria = document.getElementById("categoria");
    let nameEmpresa = document.getElementById("empresa").innerText;
    let NombreValor = nombre.value;
    let StockValor = stock.value;
    let PrecioValor = precio.value;
    let categoriaValor = categoria.value;

    if (NombreValor && StockValor && PrecioValor && categoriaValor) {
        let endpoint = "/controller/CrearProducto";

        axios.post(endpoint, {
                'producto': NombreValor,
                'stock': StockValor,
                'precio': PrecioValor,
                'empresa': nameEmpresa,
                'categoria': categoriaValor
            })
            .then(function(response) {
                console.log("Producto creado para la empresa: " + nameEmpresa);
                console.log(response);
                
                Swal.fire({
                    icon: 'success',
                    title: '¡Producto creado!',
                    text: 'El producto se ha creado exitosamente',
                    confirmButtonText: 'Aceptar'
                }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.reload();
                    }
                });
            })
            .catch(function(error) {
                console.error('Error creating product:', error);
            });
    }
}

function EliminarProducto(id) {
    let idDelete = id;
    let endpoint = "/controller/EliminarProducto";
    
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
                    'El producto ha sido eliminado.',
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

