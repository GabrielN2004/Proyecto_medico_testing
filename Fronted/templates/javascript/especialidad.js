document.addEventListener("DOMContentLoaded", function () {
    const detalles = document.querySelectorAll("details");

    detalles.forEach((detalle) => {
        detalle.addEventListener("toggle", async function () {
            if (this.open) {
                let especialidad = this.querySelector("summary").textContent.trim().toLowerCase();
                especialidad = normalizarTexto(especialidad); // Normalizar texto (elimina tildes)
                
                const id_especialidad = obtenerIdEspecialidad(especialidad); 
                
                console.log(`Especialidad seleccionada: ${especialidad}, ID: ${id_especialidad}`);

                if (!id_especialidad) {
                    console.warn("ID de especialidad no encontrado.");
                    return;
                }

                try {
                    const response = await fetch(`http://127.0.0.1:5000/turno/profesional/${id_especialidad}`);
                    if (!response.ok) {
                        console.error("Error al obtener datos:", response.status);
                        return;
                    }

                    const profesionales = await response.json();
                    console.log("Profesionales obtenidos:", profesionales);
                    actualizarCards(this, profesionales);
                } catch (error) {
                    console.error("Error en la petición:", error);
                }
            }
        });
    });

    function obtenerIdEspecialidad(nombre) {
        const especialidades = {
            "cardiologia": 1,
            "cirugia general": 2,
            "medico clinico": 3,
            "dermatologia": 4,
            "ginecologia": 5,
            "neurologia": 6,
            "pediatria": 7,
            "traumatologia": 8
        };
        return especialidades[nombre] || null;
    }

    function actualizarCards(detalle, profesionales) {
        let contenedor = detalle.querySelector(".card-info");
        if (!contenedor) {
            contenedor = document.createElement("div");
            contenedor.classList.add("card-info");
            detalle.appendChild(contenedor);
        } else {
            contenedor.innerHTML = ""; // Limpiar contenido anterior
        }

        if (profesionales.length === 0) {
            contenedor.innerHTML = "<p>No hay profesionales disponibles en esta especialidad.</p>";
            return;
        }

        profesionales.forEach((profesional) => {
            const card = document.createElement("div");
            card.classList.add("card");
            card.innerHTML = `
                <img src="/static/img/perfil.png" alt="${profesional.profesional_fullname}">
                <div class="card-info">
                    <strong>${profesional.profesional_fullname}</strong>
                    <p>Matrícula: ${profesional.profesional_matricula}</p>
                    <p>Email: ${profesional.profesional_email}</p>
                </div>
            `;
            contenedor.appendChild(card);
        });
    }

    // Función para eliminar tildes de los nombres de las especialidades
    function normalizarTexto(texto) {
        return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, ""); 
    }
});
