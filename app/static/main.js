$(document).ready(function() {
  $('.task').data('edit', false);
  $('.task div[data-view="edit"]').addClass('nodisplay');
});

$(document).on('click', '.task .actions #edit', function() {
  clickedTask = $(this).parent().parent().parent();
  handleEditTask(clickedTask, true);
});

$(document).on('click', '.task .actions #cancel-edit', function() {
  clickedTask = $(this).parent().parent().parent();
  handleEditTask(clickedTask, false);
});

$(document).on('change', '#all-tasks input, #complete-tasks input, #incomplete-tasks input', function() {
  console.log('running');
  $.ajax({
    url: '/changeTaskOrder',
    type: 'post',
    data: JSON.stringify({
      taskView: 'INCOMPLETE'
    }),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(response){
        // reload the section of the site responsible
        // for displaying the tasks.
        if (response.reload) {
          reloadTasks(response.newTaskId);
        }
    },
    error: function(error){
        console.log(error);
    }
  });
});


// AJAX request to delete a task from the database and upade the list.
$(document).on('click', '.task #delete', function() {
  $.ajax({
    url: '/deleteTask',
    type: 'post',
    data: JSON.stringify({
      parentId: $(this).parent().parent().parent().attr('id')
    }),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(response){
        // reload the section of the site responsible
        // for displaying the tasks.
        if (response.reload) {
          reloadTasks();
        }
    },
    error: function(error){
        console.log(error);
    }
  });
});

// AJAX request to edit data in the database.
$(document).on('click', '.task #submit-edit', function() {
  taskId = $(this).parent().parent().parent().attr('id');

  $.ajax({
    url: '/editTask',
    type: 'post',
    data: JSON.stringify({
      title: $('#' + taskId + ' input[name="title-input"]').val(),
      description: $('#' + taskId + ' textarea[name="description-input"]').val(),
      parentId: taskId
    }),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(response){
        // reload the section of the site responsible
        // for displaying the tasks.
        if (response.reload) {
          reloadTasks(response.newTaskId);
        }
    },
    error: function(error){
        console.log(error);
    }
  });
});

// AJAX request to add new task to the database.
$(document).on('click', '#new-task', function() {
  $.ajax({
    url: '/newTask',
    type: 'post',
    data: '',
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(response){
        // reload the section of the site responsible
        // for displaying the tasks.
        if (response.reload) {
          reloadTasks(response.newTaskId);
        }
    },
    error: function(error){
        console.log(error);
    }
  });
});

// AJAX request to add new task to the database.
$(document).on('click', '#complete, #incomplete', function() {
  if ($(this).attr('id') == 'incomplete')
    taskComplete = false;
  else
    taskComplete = true;

  $.ajax({
    url: '/changeComplete',
    type: 'post',
    data: JSON.stringify({
      parentId: $(this).parent().parent().parent().attr('id'),
      completed: taskComplete
    }),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(response){
        // reload the section of the site responsible
        // for displaying the tasks.
        if (response.reload) {
          reloadTasks();
        }
    },
    error: function(error){
        console.log(error);
    }
  });
});


// Reload all tasks on the page
function reloadTasks(taskId) {
  $('#content #content-container').load('#content #content-container', function() {
    $('.task').data('edit', false);
    $('.task div[data-view="edit"]').addClass('nodisplay');

    // if a task parameter is provided then set this
    // task to display the editing view.
    if (typeof taskId != "undefined") {
      $('.task#taskItem-' + taskId).data('edit', true);
      $('.task#taskItem-' + taskId + ' div[data-view="edit"]').removeClass('nodisplay');
      $('.task#taskItem-' + taskId + ' div[data-view="info"]').addClass('nodisplay');
    }
  });
}

function handleEditTask(target, isEdit) {
  if (!clickedTask.hasClass('task'))
    return;

  if (isEdit) {
    $('#' + clickedTask.attr('id') + '.task').data('edit', true);
    $('#' + clickedTask.attr('id') + '.task div[data-view="edit"]').removeClass('nodisplay');
    $('#' + clickedTask.attr('id') + '.task div[data-view="info"]').addClass('nodisplay');
  } else {
    $('#' + clickedTask.attr('id') + '.task').data('edit', false);
    $('#' + clickedTask.attr('id') + '.task div[data-view="edit"]').addClass('nodisplay');
    $('#' + clickedTask.attr('id') + '.task div[data-view="info"]').removeClass('nodisplay');
  }
}
