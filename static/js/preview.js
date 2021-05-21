function readImage(input) {
  var archivoInput = document.getElementById("file");
  var archivoRuta = archivoInput.value;
  var extPermitidas = /(.jpg|.jpeg|.png)$/i;
  if(!extPermitidas.exec(archivoRuta)){
      alert('Asegurese de haber seleccionado una imagen');
      archivoInput.value = '';
      return false;
    } else if ((input.files && input.files[0])) {
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
  var archivoInput = document.getElementById("archivo");
  var archivoRuta = archivoInput.value;
  var extPermitidas = /(.pdf)$/i;
  if(!extPermitidas.exec(archivoRuta)){
      alert('Asegurese de haber seleccionado un PDF');
      archivoInput.value = '';
      return false;
    }else{
      document.getElementById('datos').innerHTML = ev.target.files[0].name

      var arch = new FileReader();
      arch.addEventListener('load', leer, false);
      arch.readAsText(ev.target.files[0]);
    }
 
}

function leer(ev) {
  var editor= document.getElementById("editor");
  if(editor)
    {
    document.getElementById('editor').value = ev.target.result;
    }
  
}
//reflejar documento 

