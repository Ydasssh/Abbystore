document.addEventListener('DOMContentLoaded', function () {
    // Llamada a la API para obtener la lista de regiones
    fetch('https://api-colombia.com/api/v1/department')
        .then(response => response.json())
        .then(departamentos => {
            // Llenar el select de departamentos
            const departamentoSelect = document.getElementById('id_departamento');

            departamentoSelect.innerHTML = '<option value="">Seleccione un departamento</option>';

            departamentos.forEach(departamento => {
                const option = document.createElement('option');
                option.value = departamento.id; // Ajusta según la estructura de la respuesta de la API
                option.text = departamento.name;
                departamentoSelect.appendChild(option);
            });

            // Agregar evento de cambio al select de departamentos
            departamentoSelect.addEventListener('change', function () {
                const selectedDepartamentoId = this.value;
                cargarCiudades(selectedDepartamentoId);
            });
        })
        .catch(error => console.error('Error al obtener regiones:', error));
});

// Función para cargar dinámicamente las ciudades basadas en el departamento seleccionado
function cargarCiudades(departamentoId) {
    const ciudadSelect = document.getElementById('id_ciudad');


    // Limpiar opciones anteriores
    ciudadSelect.innerHTML = '<option value="">Seleccione una ciudad</option>';

    // Llamada a la API para obtener las ciudades del departamento seleccionado
    fetch(`https://api-colombia.com/api/v1/department/${departamentoId}/cities`)
        .then(response => response.json())
        .then(ciudades => {
            // Llenar el select de ciudades
            ciudades.forEach(ciudad => {
                const option = document.createElement('option');
                option.value = ciudad.id; // Ajusta según la estructura de la respuesta de la API
                option.text = ciudad.name;
                ciudadSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error al obtener ciudades:', error));

        var ciudadId = ciudadSelect.value;

        fetch('/registrar', {
            method: 'POST',
            body: JSON.stringify({'id_departamento': departamentoId,
        'id_ciudad': ciudadId}),
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta del servidor si es necesario
            console.log(data);
        })
        .catch(error => {
            console.error('Error al enviar la solicitud:', error);
        });
}

