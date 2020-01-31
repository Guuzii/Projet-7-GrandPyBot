
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

    insertQuestionInPage(question);

    $.post(
        '/api', // Le fichier cible côté serveur.
        {
            question : question // Paire clé: valeur à transmettre via la requete
        },
        insertResponseInPage, // Nous renseignons uniquement le nom de la fonction de retour.
        'text' // Format des données reçues.
    );    
}

function insertQuestionInPage(texte) {
    let sep = document.createElement('hr');
    let question = document.createElement('p');
    question.innerText = texte;
    question.setAttribute('class', 'text-right');

    $('#tchat-box').append(sep, question);
}

function insertResponseInPage(texte) {
    let resp = document.createElement('p');
    resp.innerText = texte;
    resp.setAttribute('class', 'text-left');

    $('#tchat-box').append(resp);
}