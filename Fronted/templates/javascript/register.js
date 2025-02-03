document.getElementById('registerForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Evita que la página se recargue

    // Capturar los datos del formulario
    const pacienteData = {
        dni_paciente: parseInt(document.getElementById('dni_paciente').value),
        paciente_name: document.getElementById('paciente_name').value,
        paciente_lastname: document.getElementById('paciente_lastname').value,
        paciente_email: document.getElementById('paciente_email').value,
        paciente_password: document.getElementById('paciente_password').value,
        id_obrasocial: parseInt(document.getElementById('id_obrasocial').value)
    };

    console.log("Datos del paciente a enviar:", pacienteData);

    try {
        // 1. Registrar el paciente
        const pacienteResult = await registrarPaciente(pacienteData);

        // 2. Registrar el usuario asociado
        const usuarioData = {
            email: pacienteData.paciente_email, // Debe venir de la respuesta
            password: pacienteData.paciente_password, // No cambiar la contraseña en la respuesta
            id_role: 3,
        };

        await registrarUsuario(usuarioData);

         // 2. Mensaje de éxito y redirección
        alert('Paciente registrado exitosamente.');
        window.location.href = '/templates/html/login.html'; // Redirige a la página de inicio de sesión

        
    } catch (error) {
        console.error('Error:', error);
        alert(error.message || 'Ocurrió un error. Inténtalo de nuevo.');
    }
});

async function registrarPaciente(pacienteData) {
    try {
        const response = await fetch('http://127.0.0.1:5000/pacientes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(pacienteData),
        });

        if (!response.ok) {
            const result = await response.json();
            throw new Error(result.error || 'Error al registrar el paciente');
        }

        const result = await response.json();
        console.log('✅ Paciente registrado:', result);

        return result; // ✅ Devuelve la respuesta correcta del servidor

    } catch (error) {
        console.error('❌ Error al registrar el paciente:', error);
        alert(error.message || 'Ocurrió un error al registrar el paciente.');
        throw error;
    }
}

async function registrarUsuario(usuarioData) {
    try {
        console.log('Datos del usuario a enviar:', usuarioData); // Para depuración

        const response = await fetch('http://127.0.0.1:5000/usuario', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(usuarioData) // ✅ Corregido
        });

        if (!response.ok) {
            const result = await response.json();
            throw new Error(result.error || 'Error al registrar el usuario');
        }

        const result = await response.json();
        console.log('✅ Usuario registrado:', result);

    } catch (error) {
        console.error('❌ Error al registrar el usuario:', error);
        alert(error.message || 'Ocurrió un error al registrar el usuario.');
    }
}
