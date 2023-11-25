$(document).ready(function() {
    var table = $('#example').DataTable({
      dom: 'lBfrtip', // l: longitud, B: botones, f: filtro, r: procesamiento, t: tabla, i: información, p: paginación
      buttons: [
        'copy', 'csv', 'excel', 'pdf', 'print'
      ]
    });

  });