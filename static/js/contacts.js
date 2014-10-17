$(document).ready(function () {

    // Following block of code is to allow ajax post requests w/ csrf tokens
    // Copy-pasted this from django website
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
                $('#add-contact-form').append(resp);
            });
        }
    });

    $('.edit-contact').click(function (e) {
        var form = $('#edit-contact-form'),
            spinner = $('#edit-spinner-modal'),
            id;

        spinner.show()

        id = $(this).parent().next().val()

        $.get('/contacts/edit/' + id + '/', function (resp) {
            $('#edit-spinner-modal').hide();
            form.html(resp);
            form.data({id: id})
        });
    });
    
    function ajax_modal_request(form_id, url) {
        var form = $(form_id),
            form_data = form.serializeObject();

        // Adds USA country code to the phone number if the number doesn't have a country code
        // Pretty fragile check. Doesn't account for whitespace in front of +
        if (form_data.phone_number[0] != '+') {
            form_data.phone_number = '+1 ' + form_data.phone_number
        }

        showSpinner();
        $.post(url, form_data, function (resp) {
            if (resp == 'Success') {
                window.location.href = "/contacts/view_all/"
            } else {
                form.html(resp);
            }
            hideSpinner();
        });
    }

    $('#submit-edit-contact-form').click(function (e) {
        var id = $('#edit-contact-form').data('id');
        ajax_modal_request('#edit-contact-form', '/contacts/edit/' + id + '/')
        e.preventDefault();
    });

    $('#submit-add-contact-form').click(function (e) {
        ajax_modal_request('#add-contact-form', '/contacts/add_contact/');
        e.preventDefault();
    });

    $('#send-messages').submit(function (e) {
        if (!confirm("Are you sure you want to send a message to every active member?")) {
            e.preventDefault();
        }
    });
})
