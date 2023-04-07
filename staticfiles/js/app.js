//Campos de los formularios
const nombre_actividad = document.querySelector("#nombre_actividad");
const btn_guardar = document.querySelector("#btn-guardar-actividad");
const participantes = document.querySelector("#participantes_actividad");
const objetivo_actividad = document.querySelector("#objetivo_actividad");
const descripcion = document.querySelector("#descripcion_actividad");
const categoria=document.querySelector('#categoria_actividad');
document.addEventListener("DOMContentLoaded", () => {
  validarFormulario();
});

function validarFormulario(e) {
  //verificamos que existan los campos
  if (
    btn_guardar &&
    nombre_actividad &&
    participantes &&
    objetivo_actividad &&
    descripcion &&
    categoria
  ) {
    btn_guardar.disabled = true;

    if (btn_guardar.disabled == true) {
      
      btn_guardar.classList.add("disabled");
    }

    nombre_actividad.addEventListener("blur", validarCampos);
    nombre_actividad.addEventListener("blur", camposLLenos);
    participantes.addEventListener("blur", validarCampos);
    participantes.addEventListener("blur", camposLLenos);
    objetivo_actividad.addEventListener("blur", validarCampos);
    objetivo_actividad.addEventListener("blur", camposLLenos);
    descripcion.addEventListener("blur", validarCampos);
    descripcion.addEventListener("blur", camposLLenos);
    categoria.addEventListener('change',validarCampos);
    categoria.addEventListener('change',camposLLenos);
  }
}

function validarCampos() {
  var errorDiv = document.getElementById("error");
  if (this.value == "") {
    errorDiv.style.display = "block";
    errorDiv.innerHTML = "Este campo es obligatorio!";
    this.style.border = "1px solid red";
    errorDiv.style.border = "2px solid red";
    btn_guardar.disabled=true;
    btn_guardar.classList.add("disabled");
    setTimeout(() => {
      errorDiv.style.display = "none";
    }, 3000);
  } else {
    errorDiv.style.display = "none";
    this.style.border = "1px solid gray";
  }
}

function camposLLenos() {
  if (
    nombre_actividad.value != "" &&
    participantes.value != "" &&
    objetivo_actividad.value != "" &&
    descripcion.value != "" &&
    categoria.value !=''
  ) {
    console.log('llenos');
    btn_guardar.disabled = false;
    btn_guardar.classList.remove("disabled");
    btn_guardar.style.opacity = 1;
  }
}
