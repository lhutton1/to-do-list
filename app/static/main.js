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
