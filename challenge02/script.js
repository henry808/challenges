$(document).ready( function() {
    $('#button').click( function() {
       var toAdd = $('input[name=checkListItem]').val();
       $('.list').prepend('<li class="item">' + toAdd + '</li>');
    });
    $(document).on('click', '.item', function() {
        $(this).remove();
    });
});