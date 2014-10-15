$(document).ready(function () {

    // Following block of code is to allow ajax post requests w/ csrf tokens
    var csrftoken = $.cookie('csrftoken');
    
    function showSpinner() {
        var spinner = $('#page-spinner').show();
    }

    function hideSpinner() {
        $('#page-spinner').hide();
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
        

    $('#add-contact').click(function () {
        // If we have already clicked on the button once, dont do the get request
        if ($('#spinner-modal').css('display') != 'none') {
            $.get('/contacts/add_contact/', function (resp) {
                $('#spinner-modal').hide();
                $('#contact-form').append(resp);
            });
        }
    });

    $('#submit-contact-form').click(function (e) {
        var form = $('#contact-form'),
            form_data = $('#contact-form').serializeObject();

        if (form_data.phone_number[0] != '+') {
            form_data.phone_number = '+1 ' + form_data.phone_number
        }

        showSpinner();
        $.post('/contacts/add_contact/', form_data, function (resp) {
            if (resp == 'Success') {
                window.location.href = "/contacts/view_all/"
            } else {
                form.html(resp);
            }
            hideSpinner();
        });
        e.preventDefault();
    });
})
