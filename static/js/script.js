$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('#description').val('');
    M.textareaAutoResize($('#description'));
  });