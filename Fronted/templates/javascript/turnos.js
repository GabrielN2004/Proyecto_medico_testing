
// Manejadores de eventos para los cambios en los selectores
function manejarCambioEspecialidades(event) {
    const id_especialidad = event.target.value;
    if (id_especialidad) {
        cargarProfesionales(id_especialidad);
    } else {
        limpiarProfesionales();
    }
}

function manejarCambioProfesionales(event) {
    const id_profesional = event.target.value;
    if (id_profesional) {
        cargarObrasociales(id_profesional); // Cargar las obras sociales
        cargarHorarios(id_profesional);    // Cargar los horarios
    } else {
        limpiarObrasociales(); // Limpiar las obras sociales si no se selecciona ningún profesional
        limpiarHorarios();    // Limpiar los horarios
    }
}

// Funciones para cargar datos de especialidades, profesionales, obras sociales y horarios
async function cargarEspecialidades() {
    try {
        const response = await fetch('http://127.0.0.1:5000/turno/especialidad');
        if (!response.ok) throw new Error("Error al obtener las especialidades");

        const especialidades = await response.json();
        console.log("Especialidades recibidas:", especialidades);

        const selectEspecialidades = document.getElementById("especialidades");
        selectEspecialidades.innerHTML = '<option value="">Seleccione una especialidad</option>';

        especialidades.forEach(especialidad => {
            const option = document.createElement("option");
            option.value = especialidad.id_especialidad;
            option.textContent = especialidad.especialidad_name;
            selectEspecialidades.appendChild(option);
        });
    } catch (error) {
        console.error("Error cargando especialidades:", error);
        alert("No se pudieron cargar las especialidades.");
    }
}

async function cargarProfesionales(id_especialidad) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/turno/profesional/${id_especialidad}`);
        if (!response.ok) throw new Error("Error al obtener los profesionales");

        const profesionales = await response.json();

        const selectProfesionales = document.getElementById("profesionales");
        selectProfesionales.innerHTML = '<option value="">Seleccione un Profesional</option>';

        profesionales.forEach(profesional => {
            const option = document.createElement("option");
            option.value = profesional.id_profesional;
            option.textContent = profesional.profesional_fullname;
            selectProfesionales.appendChild(option);
        });
    } catch (error) {
        console.error("Error cargando Profesionales:", error);
        alert("No se pudieron cargar los profesionales.");
    }
}

async function cargarObrasociales(id_profesional) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/turno/obrasocial/${id_profesional}`);
        if (!response.ok) throw new Error("Error al obtener las obras sociales");

        const obrasociales = await response.json();

        const selectObrasocial = document.getElementById("obrasociales");
        selectObrasocial.innerHTML = '<option value="">Seleccione una Obra Social</option>';

        obrasociales.forEach(obrasocial => {
            const option = document.createElement("option");
            option.value = obrasocial.id_obrasocial;
            option.textContent = obrasocial.obrasocial_name;
            selectObrasocial.appendChild(option);
        });
    } catch (error) {
        console.error("Error cargando Obras Sociales:", error);
        alert("No se pudieron cargar las obras sociales.");
    }
}

async function cargarHorarios(id_profesional) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/turno/horario_profesional/${id_profesional}`);
        if (!response.ok) throw new Error("Error al obtener los horarios");

        const horarios = await response.json();

        const selectHorarios = document.getElementById("horarios");
        selectHorarios.innerHTML = '<option value="">Seleccione un Horario</option>';

        horarios.forEach(horario => {
            const option = document.createElement("option");
            option.value = horario.id_horario;
            option.textContent = horario.horario_num;
            selectHorarios.appendChild(option);
        });
    } catch (error) {
        console.error("Error cargando Horarios:", error);
        alert("No se pudieron cargar los horarios.");
    }
}

function limpiarObrasociales() {
    const selectObrasocial = document.getElementById("obrasociales");
    selectObrasocial.innerHTML = '<option value="">Seleccione una Obra Social</option>';
}

function limpiarHorarios() {
    const selectHorarios = document.getElementById("horarios");
    selectHorarios.innerHTML = '<option value="">Seleccione un Horario</option>';
}

document.getElementById("enviarTurno").addEventListener("click", async (event) => {
    event.preventDefault();

    // Obtener la fecha del campo y convertirla al formato DD/MM/YYYY
    const fechaInput = document.getElementById("fecha_turno").value;
    const fechaParts = fechaInput.split("-");  // Descompone la fecha en partes [YYYY, MM, DD]
    const fechaFormateada = `${fechaParts[2]}/${fechaParts[1]}/${fechaParts[0]}`;  // Formato DD/MM/YYYY

    const turnoData = {
        dni_paciente: parseInt(document.getElementById("dni_paciente").value),
        id_especialidad: parseInt(document.getElementById("especialidades").value),
        id_profesional: parseInt(document.getElementById("profesionales").value),
        id_obrasocial: parseInt(document.getElementById("obrasociales").value),
        fecha_turno: fechaFormateada,  // Usamos la fecha formateada
        id_horario: parseInt(document.getElementById("horarios").value)
    };

    console.log("Datos enviados:", turnoData);

    // Función para obtener el token
    const obtenerToken = async (email) => {
        const tokenResponse = await fetch('http://127.0.0.1:5000/usuario/get_token', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ usuario_email: email })
        });

        if (!tokenResponse.ok) {
            throw new Error(`Error al obtener el token: ${tokenResponse.statusText}`);
        }

        const tokenData = await tokenResponse.json();
        console.log(tokenData)
        return tokenData.token;
    };

    // Función para crear el turno
    const crearTurno = async (token) => {
        const response = await fetch('http://127.0.0.1:5000/turno/reserva_turno', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`,
            },
            body: JSON.stringify(turnoData),
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Error al crear el turno: ${errorText}`);
        }

        return response.json();
    };

    try {
        const token = await obtenerToken(document.getElementById('usuario_email').value);
        const data = await crearTurno(token);
        console.log("Datos recibidos del servidor:", data);
        alert("Turno creado exitosamente");
    } catch (error) {
        console.error("Hubo un problema con la solicitud:", error);
        alert("No se pudo crear el turno");
    }
});



// Llamar a cargarEspecialidades cuando se cargue la página
document.addEventListener("DOMContentLoaded", cargarEspecialidades);

// Función para obtener el token
const obtenerToken = async (email) => {
    if (!email) {
        throw new Error('El email no puede estar vacío.');
    }
    const tokenResponse = await fetch('http://127.0.0.1:5000/usuario/get_token', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ usuario_email: email })
    });

    if (!tokenResponse.ok) {
        throw new Error(`Error al obtener el token: ${tokenResponse.statusText}`);
    }

    const tokenData = await tokenResponse.json();
    console.log(tokenData)
    return tokenData.token;
};

// Función para obtener los turnos de un paciente
async function obtenerTurnosPorPaciente(dni_paciente) {
    try {
        const email = document.getElementById('email_paciente_buscar').value;

        if (!email) {
            alert("Por favor, ingrese un EMAIL para buscar.");
            return;
        }

        const token = await obtenerToken(email);

        const response = await fetch(`http://127.0.0.1:5000/turno/turno_paciente/${dni_paciente}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`,
            },
        });

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error("No se encontraron turnos para este paciente.");
            }
            throw new Error(`Error al obtener los turnos: ${response.statusText}`);
        }

        const turnos = await response.json();
        console.log("Turnos recibidos:", turnos);

        if (!Array.isArray(turnos) || turnos.length === 0) {
            throw new Error("No se encontraron turnos para este paciente.");
        }

        // Llenar la tabla con los turnos obtenidos
        const tbody = document.getElementById("tbody-table-reservas");
        tbody.innerHTML = "";

        turnos.forEach(turno => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${turno.dni_paciente}</td>
                <td>${turno.fecha_turno}</td>
                <td>${turno.horario}</td>
                <td>${turno.especialidad}</td>
                <td>${turno.profesional}</td>
                <td>${turno.obrasocial}</td>
                <td>
                    <button class="button is-danger is-small eliminar-turno" data-id="${turno.id_turno}">
                        Eliminar
                    </button>
                </td>
            `;
            tbody.appendChild(fila);
        });

        // Agregar eventos de eliminación a los botones recién creados
        agregarEventosEliminar();
    } catch (error) {
        console.error("Error obteniendo los turnos:", error);
        alert(error.message);
    }
}
// Evento para buscar turnos al presionar un botón
document.getElementById("buscarTurno").addEventListener("click", (event) => {
    event.preventDefault();

    const dni_paciente = parseInt(document.getElementById("dni_paciente_buscar").value);
    console.log("DNI Paciente:", dni_paciente);  // Verifica el valor del DNI en la consola
    if (!dni_paciente) {
        alert("Por favor, ingrese un DNI para buscar.");
        return;
    }

    obtenerTurnosPorPaciente(dni_paciente);
});
// Agregar evento a los botones de eliminar cuando se renderizan los turnos
const agregarEventosEliminar = () => {
    document.querySelectorAll(".eliminar-turno").forEach((boton) => {
        boton.addEventListener("click", (event) => {
            const id_turno = event.target.getAttribute("data-id");
            if (confirm("¿Seguro que deseas eliminar este turno?")) {
                eliminarTurno(id_turno);
            }
        });
    });
};
// Función para eliminar un turno
const eliminarTurno = async (id_turno) => {
    try {
        const email = document.getElementById('email_paciente_buscar').value;

        if (!email) {
            alert("Por favor, ingrese un EMAIL para eliminar un turno.");
            return;
        }

        const token = await obtenerToken(email);

        const response = await fetch(`http://127.0.0.1:5000/turno/eliminar_turno/${id_turno}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`,
            },
        });

        if (!response.ok) {
            throw new Error(`Error al eliminar el turno: ${response.statusText}`);
        }

        const data = await response.json();
        alert(data.message);

        // Actualizar la tabla después de la eliminación
        obtenerTurnosPorPaciente(document.getElementById("dni_paciente_buscar").value);
    } catch (error) {
        console.error("Error eliminando el turno:", error);
        alert("No se pudo eliminar el turno.");
    }
};