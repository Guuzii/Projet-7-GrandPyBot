$('#form-question :input').on('keypress', (e) => {
    let keycode = e.keyCode || e.which;

    if (keycode == 13) 
    {
        e.preventDefault();
        postQuestionToApi();
    }
});

$('#send-button').click(() => {
    postQuestionToApi();    
});

function postQuestionToApi() {
    let question  = $('#question').val();

    $.post(
        '/api', // Le fichier cible côté serveur.
        {
            question : question // Nous supposons que ce formulaire existe dans le DOM.
        },
        insertInPage, // Nous renseignons uniquement le nom de la fonction de retour.
        'text' // Format des données reçues.
    );
}

function insertInPage(texte) {
    $('#user-question').text(texte);
}