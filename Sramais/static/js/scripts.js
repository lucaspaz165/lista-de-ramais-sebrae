console.log('funcionou!');
  var baseUrl   = 'http://127.0.0.1:8000/';
 var searchBtn = $('#search-btn');
 var searchForm = $('#search-form');
 var filter     = $('#filter');
 $(searchBtn).on('click', function() {
        searchForm.submit();
    });

$('.datepicker').datepicker({
    format: 'dd/mm/yyyy',
    language: 'pt-BR'
});

<a class="confirm-delete">Delete</a>
$(document).on('click', '.confirm-delete', function(){
    return confirm('Voce deseja deletar esse ramal ?');
})
