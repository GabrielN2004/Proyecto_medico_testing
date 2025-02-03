
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir el comportamiento por defecto del formulario

    // Obtener los valores del formulario
    const email = document.getElementById('paciente_email').value;
    const password = document.getElementById('paciente_password').value;

    // Crear el objeto con los datos del usuario
    const userData = {
        email: email,
        password: password
    };

    // Realizar la solicitud de login a la API Flask
    fetch('http://localhost:5000/auth/login', {  
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            // Si el login es exitoso, guardar el token en el localStorage
            localStorage.setItem('auth_token', data.token);
            // Decodificar el token para obtener el id_usuario
            alert('Login exitoso');

            // Redirigir a la página protegida o al home
            window.location.href = '/templates/html/index.html';  // Cambia la URL según la página a la que quieras redirigir
        } else {
            // Si el login falla, mostrar un mensaje de error
            alert('Correo o contraseña incorrectos');
        }
    })
    .catch(error => {
        console.error('Error en el login:', error);
        alert('Hubo un error al intentar hacer login. Por favor, inténtalo de nuevo.');
    });
});
