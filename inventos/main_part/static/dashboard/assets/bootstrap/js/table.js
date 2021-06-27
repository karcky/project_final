$(document).ready(function () {
    $('#example1').DataTable({
      "paging": false // false to disable pagination (or any other option)
    });
    $('.dataTables_length').addClass('bs-select');
  });