async function runOne() {
  const usuario = "cinthiavota";
  const contraseña = "1234";

  const loginResponse = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ usuario, contraseña })
  });

  const loginData = await loginResponse.json();
  const loginOutput = document.querySelector(".print.p1");
  loginOutput.textContent = loginData.mensaje;

  if (loginResponse.ok) {
    verificarSesion();
  }
}

async function mostrarTareas() {
  const tareasOutput = document.querySelector(".print.p3");

  try {
    const response = await fetch("/tareas");
    const data = await response.json();

    if (!Array.isArray(data)) {
      tareasOutput.innerHTML = `<p class="code">${data.mensaje}</p>`;
      return;
    }

    if (data.length === 0) {
      tareasOutput.innerHTML = `<p class="code">No hay tareas registradas.</p>`;
      return;
    }

    const lista = data.map(t => `<li><strong>${t.titulo}</strong>: ${t.descripcion}</li>`).join("");
    tareasOutput.innerHTML = `<ul class="code">${lista}</ul>`;
  } catch (error) {
    tareasOutput.innerHTML = `<p class="code">Error al obtener las tareas.</p>`;
  }
}

async function cerrarSesion() {
  const response = await fetch("/logout", { method: "POST" });
  const data = await response.json();

  alert(data.mensaje);

  document.querySelector(".print.p1").textContent = "";
  document.querySelector(".print.p3").innerHTML = `<p class="code">Sesión cerrada.</p>`;

  verificarSesion();
}

async function verificarSesion() {
  const btnLogin = document.getElementById("btn-login");
  const btnLogout = document.getElementById("btn-logout");

  try {
    const response = await fetch("/tareas");
    const data = await response.json();

    if (Array.isArray(data)) {
      btnLogin.style.display = "none";
      btnLogout.style.display = "inline-block";
      mostrarTareas(); // Mostrar tareas si hay sesión
    } else {
      btnLogin.style.display = "inline-block";
      btnLogout.style.display = "none";
    }
  } catch {
    btnLogin.style.display = "inline-block";
    btnLogout.style.display = "none";
  }
}

// Ejecutar al cargar la página
window.onload = verificarSesion;
