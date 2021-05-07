function readImage(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      $('#preview').attr('src', e.target.result); // Renderizamos la imagen
    }
    reader.readAsDataURL(input.files[0]);
  }
}

$("#file").change(function () {
  // Código a ejecutar cuando se detecta un cambio de archivO
  readImage(this);
});

//reflejar documento 
window.addEventListener('load', inicio, false);

function inicio() {
  var archivo = document.getElementById("archivo");
  if(archivo)
  {
    document.getElementById('archivo').addEventListener('change', cargar, false);
  }
  
}

function cargar(ev) {
  document.getElementById('datos').innerHTML = ev.target.files[0].name

  var arch = new FileReader();
  arch.addEventListener('load', leer, false);
  arch.readAsText(ev.target.files[0]);
}

function leer(ev) {
  var editor= document.getElementById("editor");
  if(editor)
    {
    document.getElementById('editor').value = ev.target.result;
    }
  
}
//reflejar documento 
