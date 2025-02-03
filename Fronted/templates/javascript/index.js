document.getElementById("verPerfil").addEventListener("click", () => {
    const token = localStorage.getItem("auth_token"); // Usar el mismo nombre de clave que en el login
    if (token) {
        window.location.href = "/templates/html/perfil.html"; // Asegurar la ruta correcta del perfil
    } else {
        alert("Debes iniciar sesión para ver tu perfil");
        window.location.href = "/templates/html/login.html"; // Asegurar la ruta correcta del login
    }
});
