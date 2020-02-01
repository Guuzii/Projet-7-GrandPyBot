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
        'json' // Format des données reçues.
    );    
}

function insertQuestionInPage(texte) {
    let div = document.createElement('div');
    let sep = document.createElement('hr');
    let question = document.createElement('p');
    question.innerText = texte;

    div.setAttribute('class', 'row question')
    div.append(sep, question)

    $('#tchat-box').append(div);
}

function insertResponseInPage(query_resp) {
    let resp_div = document.createElement('div');
    let map_div = document.createElement('div');
    let map_iframe = document.createElement('iframe');
    let resp = document.createElement('p');
    resp.innerText = query_resp['texte'];

    map_iframe.setAttribute('width', '800');
    map_iframe.setAttribute('height', '250');
    map_iframe.setAttribute('frameborder', '0');
    map_iframe.setAttribute('src', "https://www.google.com/maps/embed/v1/place?q=" + query_resp['map_query'] + "&key=AIzaSyDP9USsAbkxBmQibnOAYxTnDA01uXyUWRU")

    map_div.setAttribute('class', 'map-container')
    map_div.append(map_iframe)

    resp_div.setAttribute('class', 'row bot-answer')
    resp_div.append(resp, map_div)

    $('#tchat-box').append(resp_div);
}