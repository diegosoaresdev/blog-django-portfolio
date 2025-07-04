// static/js/app.js
$(document).ready(function(){
    // Mostra ou esconde o botão "Voltar ao Topo"
    $(window).scroll(function(){
        if ($(this).scrollTop() > 200) {
            $('#scrollTopBtn').fadeIn();
        } else {
            $('#scrollTopBtn').fadeOut();
        }
    });

    // Animação de scroll ao clicar no botão
    $('#scrollTopBtn').click(function(){
        $('html, body').animate({scrollTop : 0}, 600);
        return false;
    });
});