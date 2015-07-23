$(document).ready(function() {
    
    //Personalização das mensagens de erro do login para os campos de email
    var elements = document.getElementsByName("email");
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {            
                e.target.setCustomValidity("Por favor, insira seu e-mail neste campo.");
            }
        };
        elements[i].oninput = function(e) {
            e.target.setCustomValidity("");
        };
    }    
    //Idem do item acima mas para o Campo senha
    var elements = document.getElementsByName("pass");
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (e.target.validity.valueMissing) {
                e.target.setCustomValidity("Por favor, insira sua senha neste campo.");
            }
        };
        elements[i].oninput = function(e) {
            e.target.setCustomValidity("");
        };
    }    
    
    $( ".item-cat" ).click(function() {
        $('#d_categoria span').html($(this).html());
        return false;
    });    
})



