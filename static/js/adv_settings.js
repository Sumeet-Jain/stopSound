$(document).ready(function () {
    var manual_choice = document.querySelector('[value=manual]');

    function move_sound_widget(e) {
        var sound_widget = document.getElementById('id_sound_level');
        if (this.checked) {
            this.parentNode.parentNode.appendChild(sound_widget);
            sound_widget.type = 'input';
            sound_widget.style.display = "inline-block";
        }
    };

    move_sound_widget.call(manual_choice);

    $(manual_choice).click(function (e) {
        move_sound_widget.call(this)
    });

    $('[value=auto']).click(function (e) {
        $('#id_sound_level').hide()
    });

    $('[value=auto-save]').click(function (e) {
        $('#id_sound_level').hide()
    });
});
