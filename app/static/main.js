$(document).ready(function() {
  $('.task').data('edit', false);
  $('.task div[data-view="edit"]').addClass('nodisplay');

  currentFilter = new URL(window.location).searchParams.get('filterBy');

  if ( currentFilter == 'complete')
    document.querySelector('#complete-tasks input').checked = true;
  else if (currentFilter == 'incomplete')
    document.querySelector('#incomplete-tasks input').checked = true;
  else
    document.querySelector('#all-tasks input').checked = true;
});

$(document).on('click', '#all-tasks', function() {
  window.location = "/?filterBy=all";
});

$(document).on('click', '#complete-tasks', function() {
  window.location = "/?filterBy=complete";
});

$(document).on('click', '#incomplete-tasks', function() {
  window.location = "/?filterBy=incomplete";
});
