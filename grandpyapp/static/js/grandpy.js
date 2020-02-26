// Prevent default action on pressing enter key and make it call postQuestionToApi() instead.
$('#form-question :input').on('keypress', (e) => {
    let keycode = e.keyCode || e.which;

    if (keycode == 13) 
    {
        e.preventDefault();
        postQuestionToApi();
    }
});

// Listening to click event on the send button. Call postQuestionToApi().
$('#send-button').click(() => {
    postQuestionToApi();    
});

// Get question entered by the user and send a post request to the route /api using jquery
function postQuestionToApi() {
    let question  = $('#question').val();

    insertQuestionInPage(question);

    $('#loading-spinner').css('display', 'flex'); // show loading spinner

    $.post(
        '/api', // targeted file on server
        {
            question : question // data to send with request (key: value)
        },
        insertResponseInPage, // name of the function that will handle the response
        'json' // data format from the response
    );    
}

// Insert user's question in the view
function insertQuestionInPage(texte) {

    let div = document.createElement('div');
    let sep = document.createElement('hr');
    let question = document.createElement('p');

    if (texte && texte.replace(/\s/g, "") != "") // Check if question is not null or empty
    {
        question.innerText = texte;
    }
    else
    {
        question.innerText = 'Question vide';
    }    

    div.setAttribute('class', 'row question');
    div.append(sep, question);

    $('#tchat-box').append(div);
}

// Insert texte depending on the response from the request
function insertResponseInPage(query_resp) {
    
    let resp_div = document.createElement('div');
    resp_div.setAttribute('class', 'row bot-answer');

    let resp = document.createElement('p');

    if (query_resp['adress']) 
    {
        resp.innerText = "Voila l'adresse que tu m'a demandé : " + query_resp['adress'] + "\n" + query_resp['texte'];

        let map_div = document.createElement('div');
        let map_iframe = document.createElement('iframe');
        map_iframe.setAttribute('width', '800');
        map_iframe.setAttribute('height', '250');
        map_iframe.setAttribute('frameborder', '0');
        map_iframe.setAttribute('src', "https://www.google.com/maps/embed/v1/place?q=" + query_resp['map_query'] + "&key=AIzaSyDP9USsAbkxBmQibnOAYxTnDA01uXyUWRU");

        map_div.setAttribute('class', 'map-container');
        map_div.append(map_iframe);
        
        setTimeout(() => { // hide loading spinner after 1 second
            $('#loading-spinner').hide();
            resp_div.append(resp, map_div);
        }, 1000);
    }
    else 
    {
        resp.innerText = query_resp['texte'];

        setTimeout(() => { // hide loading spinner after 1 second
            $('#loading-spinner').hide();
            resp_div.append(resp);
        }, 1000);
    }
    
    $('#tchat-box').append(resp_div);
}