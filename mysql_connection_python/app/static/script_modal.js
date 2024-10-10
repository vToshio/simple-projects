$(document).ready(function() {
    $('#modalRemover').on('show.bs.modal', function(event) {
        var btn = $(event.relatedTarget);
        var user_id = btn.data('task-id');
        var titulo = 'Editar Usuário (ID ' + user_id + ')'
        $('#titulo-remover').text(titulo);
        $('#modalRemover input[name=user_id]').val(user_id);
    });
});