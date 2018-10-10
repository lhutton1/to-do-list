// on the click of a button on a task, create an AJAX request
// to the server.
$(document).on('click', '.task .actions button', function() {
  $.ajax({
    url: '/respond',
    type: 'post',
    data: JSON.stringify({
      id: $(this).attr('id'),
      parentId: $(this).parent().parent().attr('id')
    }),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(response){
        // reload the section of the site responsible
        // for displaying the tasks.
        $('#content').load('#content #content-container');
        console.log(response);
    },
    error: function(error){
        console.log(error);
    }
  });
});
