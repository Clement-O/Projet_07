// jQuery Script


$(function () {
    $('#form').on('submit', function (event) {
        event.preventDefault();
        validation($(this).serializeArray());
    });

    function validation(input){
        if ($.trim($('#formInput').val())) {
            $('#pageLeft').css('flex-direction', 'column');
            displayLoading();
            post(input)
        }
        else {
            $('#form')[0].reset()
        }
    }

    function post(input) {
        $.post(
            '/process', input
        ).done(function(response) {
            hideLoading();
            if (response['status'] === 'OK') {
                displayResult(response)
            }
            else {
                displayError();
                $('#wikiTitle').text(response['message'])
            }
        })
    }

    function displayError() {
        $('#map').css('display', 'none');
        $('#wikiSummary').text("");
        $('#wikiSource').text("")
    }

    function displayLoading() {
        $('#map').css('display', 'none');
        $('#loading').css('display', 'block');
    }

    function hideLoading() {
        $('#loading').css('display', 'none');
        $('#map').css('display', 'block');
    }

    function displayResult(response) {
        let sentence = response['wiki_source'] + " de GrandPy, ";
        $('#mapTitle').text(response['formatted_address']);
        $('#mapGoogle').attr('src', response['map_url']);
        $('#wikiTitle').text(response['wiki_title']);
        $('#wikiSummary').text(response['wiki_summary']);
        $('#wikiSource').text(sentence);
        $('#wikiSource').append('<a id="wiki_url" target="_blank">Wikipedia</a>');
        $('#wiki_url').attr('href', response['wiki_url'])
    }

});