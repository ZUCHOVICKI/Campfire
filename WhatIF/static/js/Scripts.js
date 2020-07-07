// INICIALIZAR DROP MENU
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var options = {};
    var instances = M.Dropdown.init(elems, options);
  });
//INICIALIZAR MODAL
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    options = {}
    var instances = M.Modal.init(elems, options);
  });


 //INICIALIZAR SELECTS 
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    options = {}
    var instances = M.FormSelect.init(elems, options);
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


  ContestarPregunta =  () =>{
      
    let DescripcionPregunta = document.getElementById('DescripcionPregunta')

    // let AutorRespuesta = document.getElementById('Userid').dataset.idUser
    let PreguntaRespuesta = document.getElementById('Preguntaid').dataset.idpregunta

    let formData = new FormData();
 formData.append("csrfmiddlewaretoken",getCookie("csrftoken"));
 formData.append("DescripcionPregunta",DescripcionPregunta.value);
//  formData.append("AutorRespuesta",AutorRespuesta);
 formData.append("PreguntaRespuesta",PreguntaRespuesta);
 

//  console.log(AutorRespuesta)
 $.ajax({

    type:"POST",
    url:"http://localhost:8000/CampfireQuestions/NuevaRespuesta",
    data: formData,
    
    processData : false,
    contentType  : false,
    success : function(data){
         console.log(data)
         window.location.reload(false); 
    },
    error: function(data){
        console.log(data)
        alert("Ha ocurrido un error")
    }
    
}); 
DescripcionPregunta.value = ""
  } 

  BorrarPregunta = () =>{

    let ID = document.getElementById('IdBorrar').dataset.idborrar
    
    let formData = new FormData()
    formData.append("csrfmiddlewaretoken",getCookie("csrftoken"));
    formData.append("ID",ID);

    $.ajax({

        type:"POST",
        url:"http://localhost:8000/CampfireQuestions/BorrarPregunta",
        data: formData,
        
        processData : false,
        contentType  : false,
        success : function(data){
             console.log(data)

             Swal.fire({
                title: "Exito",
                text: "Se a Borrado correctamente",
                icon: 'success',
                confirmButtonText: 'Continuar'
              }).then((result) => {
                if (result.value) {
                    window.location = "http://localhost:8000/CampfireQuestions/HomeQA"
                  
                }})
                
        },
        error: function(data){
            console.log(data)
            alert("Ha ocurrido un error")
        }
        
    });

    
   
  }


  CrearPregunta = () =>{

    Titulo = document.getElementById('NombrePregunta').value
    Descripcion = document.getElementById('DescripcionPregunta').value
    Categoria =document.getElementById('CategoriaPregunta').value

    let formData = new FormData()
    formData.append("csrfmiddlewaretoken",getCookie("csrftoken"));
    formData.append("Titulo",Titulo);
    formData.append("Descripcion",Descripcion);
    formData.append("Categoria",Categoria);
    
    $.ajax({

        type:"POST",
        url:"http://localhost:8000/CampfireQuestions/NuevaPregunta",
        data: formData,
        
        processData : false,
        contentType  : false,
        success : function(data){
             console.log(data)

             Swal.fire({
                title: "Exito",
                text: "Se a Agregado correctamente",
                icon: 'success',
                confirmButtonText: 'Continuar'
              }).then((result) => {
                if (result.value) {
                    window.location = "http://localhost:8000/CampfireQuestions/HomeQA"
                  
                }})
                
        },
        error: function(data){
            console.log(data)
            alert("Ha ocurrido un error")
        }
        
    });

  }


  CambiarContraseña = () =>{

    Contraseña = document.getElementById('ContraseñaPerfil').value

    ContraseñaConf = document.getElementById('ContraseñaPerfilConf').value

    formData = new FormData()

    formData.append("csrfmiddlewaretoken",getCookie("csrftoken"));
    formData.append("Contraseña",Contraseña)

    if (Contraseña == ContraseñaConf){
      
      if(Contraseña.length>5){

        $.ajax({

            type:"POST",
            url:"http://localhost:8000/CambioContraseña",
            data: formData,
            
            processData : false,
            contentType  : false,
            success : function(data){
                 console.log(data)
    
                 Swal.fire({
                    title: "Exito",
                    text: "Se a Cambiado correctamente",
                    icon: 'success',
                    confirmButtonText: 'Continuar'
                  }).then((result) => {
                    if (result.value) {
                        window.location = "http://localhost:8000/Perfil"
                      
                    }})
                    
            },
            error: function(data){
                console.log(data)
                alert("Ha ocurrido un error")
            }
            
        });
    }
  
  else{

    Swal.fire({
      title: "Error",
          text: "Las Contraseñas Necesita Un Minimo de 6 Caracteres",
          icon: 'error',
          confirmButtonText: 'Continuar'
  })

  }
  }
    else{

        Swal.fire({
            title: "Error",
                text: "Las Contraseñas no Conciden",
                icon: 'error',
                confirmButtonText: 'Continuar'
        })
    }
  }


  CambiarFoto = () => {

    fotoNew = document.getElementById('FotoPerfil').files[0];

    formData = new FormData()
    formData.append("csrfmiddlewaretoken",getCookie("csrftoken"));
    formData.append("Foto",fotoNew)

    $.ajax({

        type:"POST",
        url:"http://localhost:8000/Cambiofoto",
        data: formData,
        
        processData : false,
        contentType  : false,
        success : function(data){
             console.log(data)

             Swal.fire({
                title: "Exito",
                text: "Se a Cambiado correctamente",
                icon: 'success',
                confirmButtonText: 'Continuar'
              }).then((result) => {
                if (result.value) {
                    window.location = "http://localhost:8000/Perfil"
                  
                }})
                
        },
        error: function(data){
            console.log(data)
            alert("Ha ocurrido un error")
        }
        
    });
  }