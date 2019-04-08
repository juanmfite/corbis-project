$( document ).ready(function() {

    $("#deleteArticulo").click(function (val) {

        console.log($(this).attr("value"));
        articulo_id = $(this).attr("value");

        swal("Esta seguro que quiere eliminar el articulo?", {
            buttons: {
              cancel: "No",
              catch: {
                text: "Si",
                value: "catch",
              },
              defeat: false,
            },
          })
          .then((value) => {
            switch (value) {           
              case "catch":
              $.ajax({
                  url: '/deleteArticulo/'+articulo_id.toString(),
                  type: 'GET',
                  success:function(art) {
                    swal("El articulo ha sido eliminado", "-", "success");
                  }
              });
                
                break;
            }
          });
          
          console.log("Termino")
                                 
    });


});