$( document ).ready(function() {
    console.log( "ready!" );

    $("#deleteArticulo").click(function () {

        console.log("HOLA")

        // $.ajax({
        //     url: api_url + '/datos/datosDisponibles',
        //     type: 'GET',
        //     data: fechas,
        //     success:function(result) {
        //         if (result.disponible) {
        //             swal({
        //                 title: "Hay datos disponibles",
        //                 icon: "success",
        //                 timer: 1500,
        //             });
        //         } 
        //         else{
        //             swal({
        //                 title: "No hay datos disponibles",
        //                 icon: "error",
        //                 timer: 1500,
        //             });
        //         }
        //     }
        // });                              
    });


});