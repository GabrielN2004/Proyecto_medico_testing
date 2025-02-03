console.log(localStorage);

document.addEventListener("DOMContentLoaded", () => {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const pacienteDNIInput = document.getElementById('dni_paciente');
    const pacienteNameInput = document.getElementById('paciente_name');
    const pacienteLastnameInput = document.getElementById('paciente_lastname');
    const idObrasocialSelect = document.getElementById('id_obrasocial');

    const btnModificar = document.querySelector('.Modi-btn');
    const btnEliminar = document.querySelector('.trash-btn');
    const btnCerrarSesion = document.querySelector('.btn-profile');

    // Función para obtener los datos del paciente
    const obtenerDatosPaciente = async () => {
        try {
            const token = localStorage.getItem("auth_token");
            if (!token) {
                alert("No se ha encontrado un token de autenticación.");
                return;
            }
            const response = await fetch('http://127.0.0.1:5000/user/profile', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                }
            });
            const result = await response.json();
            if (response.status === 200) {
                // Llenar los campos con los datos obtenidos
                emailInput.value = result.paciente_email;
                pacienteDNIInput.value = result.dni_paciente
                pacienteNameInput.value = result.paciente_name;
                pacienteLastnameInput.value = result.paciente_lastname;
                // Si tienes más campos, puedes agregarlos de la misma manera
                idObrasocialSelect.value = result.id_obrasocial; // Ejemplo de otro campo
            } else {
                alert(result.error || 'Error al obtener los datos del paciente');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Hubo un error al obtener los datos del paciente.');
        }
    };

    // Llamar a obtener los datos al cargar la página
    obtenerDatosPaciente();

    // Función para realizar la solicitud PUT de modificar datos del paciente
    async function modificarPerfil(data) {
        try {
            const token = localStorage.getItem("auth_token");
            if (!token) {
                alert("No se ha encontrado un token de autenticación.");
                return;
            }
            const response = await fetch('http://127.0.0.1:5000/user/modificar', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify(data)
            });
            const result = await response.json();
            if (response.status === 200) {
                alert('Perfil actualizado con éxito');
            } else {
                alert(result.error || 'Error al actualizar el perfil');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Hubo un error al realizar la solicitud.');
        }
    }

    // Función para eliminar la cuenta del paciente
    async function eliminarCuenta() {
        try {
            const token = localStorage.getItem("auth_token");
            if (!token) {
                alert("No se ha encontrado un token de autenticación.");
                return;
            }
            const response = await fetch('http://127.0.0.1:5000/user/eliminar', {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${token}`,
                }
            });
            const result = await response.json();
            if (response.status === 200) {
                alert('Cuenta eliminada con éxito');
                window.location.href = '/templates/html/login.html'; // Redirigir al login después de eliminar la cuenta
            } else {
                alert(result.error || 'Error al eliminar la cuenta');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Hubo un error al eliminar la cuenta.');
        }
    }

    // Función para cerrar sesión (invalida el token)
    async function cerrarSesion() {
        try {
            const token = localStorage.getItem("auth_token");
            if (!token) {
                alert("No se ha encontrado un token de autenticación.");
                return;
            }
            const response = await fetch('http://127.0.0.1:5000/user/cerrar_sesion', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                }
            });
            const result = await response.json();
            if (response.status === 200) {
                alert('Sesión cerrada');
                localStorage.removeItem('token'); // Eliminar el token del almacenamiento local
                window.location.href = '/login'; // Redirigir al login
            } else {
                alert(result.error || 'Error al cerrar sesión');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Hubo un error al cerrar sesión.');
        }
    }

    // Lógica para manejar el formulario de modificación
    btnModificar.addEventListener('click', async (e) => {
        e.preventDefault();
        const data = {
            nombre: pacienteNameInput.value,
            apellido: pacienteLastnameInput.value,
            email: emailInput.value,
            password: passwordInput.value
        };
        modificarPerfil(data);
    });

    // Lógica para eliminar cuenta
    btnEliminar.addEventListener('click', () => {
        if (confirm('¿Estás seguro de que deseas eliminar tu cuenta?')) {
            eliminarCuenta();
        }
    });

    // Lógica para cerrar sesión
    btnCerrarSesion.addEventListener('click', () => {
        if (confirm('¿Estás seguro de que deseas cerrar sesión?')) {
            cerrarSesion();
        }
    });
});
