function CrearEmpresa() {
    let EmpresaNombre = document.getElementById("nombre_empresa");
    let EmpresaPeriodo = document.getElementById("periodo_actividad");
    let EmpresaEstado = document.getElementById("ESTADO");

    let nombre = EmpresaNombre.value;
    let periodo = EmpresaPeriodo.value;
    let estado = EmpresaEstado.value;

    let endpoint = "/controller/CrearEmpresa";
    if (nombre && periodo && estado) {
        axios.post(endpoint, {
                'nombre': nombre,
                'periodo': periodo,
                'estado': estado
            })
            .then(function(response) {
                console.log(response);
                window.location.reload();
            })
            .catch(function(error) {
                console.error('Error creating product:', error);
            });
    }
}

document.querySelectorAll('.btnEliminarEmpresa').forEach(item => {
    item.addEventListener('click', event => {
        const id = event.target.dataset.id;
        // Aquí puedes agregar el código para eliminar la empresa con el id obtenido
    });
});



function EditarEmpresa() {
    let EmpresaNombre = document.getElementById("nombre_empresa_editar");
    let EmpresaPeriodo = document.getElementById("periodo_actividad_editar");
    let EmpresaEstado = document.getElementById("estado_editar");
    let EmpresaId = document.getElementById("id_empresa_editar");

    let nombre = EmpresaNombre.value;
    let periodo = EmpresaPeriodo.value;
    let estado = EmpresaEstado.value;
    let id = EmpresaId.value;

    let endpoint = "/controller/EditarEmpresa";
    if (nombre && periodo && estado && id) {
        axios.post(endpoint, {
                'id': id,
                'nombre': nombre,
                'periodo': periodo,
                'estado': estado
            })
            .then(function(response) {
                console.log(response);
                window.location.reload();
            })
            .catch(function(error) {
                console.error('Error editing product:', error);
            });
    }
}

function cerrarFormularioEditar() {
    document.getElementById('modalEditar').style.display = 'none';
}
